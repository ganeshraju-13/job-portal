from django.shortcuts import render
from .models import Job, Application
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def job_list(request):

    query = request.GET.get('q', '').strip()

    if query:
        jobs = Job.objects.filter(
            Q(title__icontains=query) |
            Q(company__icontains=query) |
            Q(location__icontains=query)
        )
    else:
        jobs = Job.objects.all()

    return render(request, 'jobapp/job_list.html', {
        'jobs': jobs
    })


def job_detail(request, id):

    job = Job.objects.get(id=id)

    return render(request, 'jobapp/job_detail.html', {
        'job': job
    })


@login_required
def edit_job(request, id):

    if not request.user.is_staff:
        return render(request, 'jobapp/job_list.html', {
            'jobs': Job.objects.all()
        })

    job = Job.objects.get(id=id)

    if request.method == 'POST':

        job.title = request.POST['title']
        job.company = request.POST['company']
        job.location = request.POST['location']
        job.description = request.POST['description']
        job.salary = request.POST['salary']

        job.save()

        messages.success(
            request,
            'Job updated successfully!'
        )

        return render(request, 'jobapp/job_detail.html', {
            'job': job
        })

    return render(request, 'jobapp/edit_job.html', {
        'job': job
    })


@login_required
def delete_job(request, id):

    if not request.user.is_staff:
        return render(request, 'jobapp/job_list.html', {
            'jobs': Job.objects.all()
        })

    job = Job.objects.get(id=id)

    if request.method == 'POST':

        job.delete()

        messages.success(
            request,
            'Job deleted successfully!'
        )

        return render(request, 'jobapp/job_list.html', {
            'jobs': Job.objects.all()
        })

    return render(request, 'jobapp/delete_job.html', {
        'job': job
    })


@login_required
def apply_job(request, id):

    job = Job.objects.get(id=id)

    existing_application = Application.objects.filter(
        user=request.user,
        job=job
    ).first()

    if existing_application:

        messages.warning(
            request,
            'You have already applied for this job.'
        )

        return render(
            request,
            'jobapp/application_status.html',
            {
                'application': existing_application
            }
        )

    if request.method == 'POST':

        resume = request.FILES.get('resume')

        allowed_types = [
            'application/pdf',
            'application/msword',
            'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        ]

        if not resume:

            messages.warning(
                request,
                'Please upload your resume.'
            )

            return render(
                request,
                'jobapp/apply.html',
                {
                    'job': job
                }
            )

        max_size = 5 * 1024 * 1024

        if resume.size > max_size:

            messages.warning(
                request,
                'Resume file size must be less than 5 MB.'
            )

            return render(
                request,
                'jobapp/apply.html',
                {
                    'job': job
                }
            )

        if resume.content_type not in allowed_types:

            messages.warning(
                request,
                'Please upload only PDF, DOC, or DOCX files.'
            )

            return render(
                request,
                'jobapp/apply.html',
                {
                    'job': job
                }
            )

        application = Application.objects.create(
            user=request.user,
            job=job,
            name=request.POST['name'],
            email=request.POST['email'],
            resume=resume,
            cover_letter=request.POST['cover_letter']
        )

        messages.success(
            request,
            'Application submitted successfully!'
        )

        return render(
            request,
            'jobapp/application_success.html',
            {
                'job': job,
                'application': application
            }
        )

    return render(
        request,
        'jobapp/apply.html',
        {
            'job': job
        }
    )


@login_required
def application_status(request, id):

    application = Application.objects.get(
        id=id,
        user=request.user
    )

    return render(
        request,
        'jobapp/application_status.html',
        {
            'application': application
        }
    )


@login_required
def my_applications(request):

    applications = Application.objects.filter(
        user=request.user
    ).order_by('-id')

    return render(
        request,
        'jobapp/my_applications.html',
        {
            'applications': applications
        }
    )


def register(request):

    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():

            return render(
                request,
                'jobapp/register.html',
                {
                    'error':
                    'Username already exists. Please choose another username.'
                }
            )

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        login(request, user)

        messages.success(
            request,
            'Registration successful! Welcome to Job Portal.'
        )

        return render(
            request,
            'jobapp/job_list.html',
            {
                'jobs': Job.objects.all()
            }
        )

    return render(
        request,
        'jobapp/register.html'
    )


def logout_user(request):

    logout(request)

    messages.success(
        request,
        'You have been logged out successfully.'
    )

    return render(
        request,
        'jobapp/job_list.html',
        {
            'jobs': Job.objects.all()
        }
    )


def login_user(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            messages.success(
                request,
                'Login successful!'
            )

            return render(
                request,
                'jobapp/job_list.html',
                {
                    'jobs': Job.objects.all()
                }
            )

        return render(
            request,
            'jobapp/login.html',
            {
                'error': 'Invalid username or password.'
            }
        )

    return render(
        request,
        'jobapp/login.html'
    )


@login_required
def admin_applications(request):

    if not request.user.is_staff:

        return render(
            request,
            'jobapp/job_list.html',
            {
                'jobs': Job.objects.all()
            }
        )

    applications = Application.objects.all().order_by('-id')

    return render(
        request,
        'jobapp/admin_applications.html',
        {
            'applications': applications
        }
    )


@login_required
def update_application_status(request, id):

    if not request.user.is_staff:

        return render(
            request,
            'jobapp/job_list.html',
            {
                'jobs': Job.objects.all()
            }
        )

    application = Application.objects.get(id=id)

    if request.method == 'POST':

        status = request.POST['status']

        application.status = status
        application.save()

        messages.success(
            request,
            'Application status updated successfully!'
        )

    return render(
        request,
        'jobapp/admin_applications.html',
        {
            'applications':
            Application.objects.all().order_by('-id')
        }
    )


@login_required
def admin_application_detail(request, id):

    if not request.user.is_staff:

        return render(
            request,
            'jobapp/job_list.html',
            {
                'jobs': Job.objects.all()
            }
        )

    application = Application.objects.get(id=id)

    return render(
        request,
        'jobapp/admin_application_detail.html',
        {
            'application': application
        }
    )


@login_required
def admin_dashboard(request):

    if not request.user.is_staff:

        return render(
            request,
            'jobapp/job_list.html',
            {
                'jobs': Job.objects.all()
            }
        )

    total_jobs = Job.objects.count()

    total_applications = Application.objects.count()

    pending_applications = Application.objects.filter(
        status='Pending'
    ).count()

    shortlisted_applications = Application.objects.filter(
        status='Shortlisted'
    ).count()

    rejected_applications = Application.objects.filter(
        status='Rejected'
    ).count()

    return render(
        request,
        'jobapp/admin_dashboard.html',
        {
            'total_jobs': total_jobs,
            'total_applications': total_applications,
            'pending_applications': pending_applications,
            'shortlisted_applications': shortlisted_applications,
            'rejected_applications': rejected_applications,
        }
    )