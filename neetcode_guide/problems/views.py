from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Problem, Attempt
from .forms import AttemptForm

def home(request):
    difficulty_filter = request.GET.get('difficulty', '')
    topic_filter = request.GET.get('topic', '')
    status_filter = request.GET.get('status', '')
    search_query = request.GET.get('search', '')

    problems = Problem.objects.all()
    
    if difficulty_filter:
        problems = problems.filter(difficulty=difficulty_filter)
    
    if topic_filter:
        problems = problems.filter(topic__icontains=topic_filter)
    
    if search_query:
        problems = problems.filter(
            Q(title__icontains=search_query) | 
            Q(topic__icontains=search_query)
        )
    
    if status_filter == 'solved':
        solved_problem_ids = []
        for problem in problems:
            latest_attempt = Attempt.objects.filter(problem=problem).order_by('-date_attempted').first()
            if latest_attempt and latest_attempt.status == 'Solved':
                solved_problem_ids.append(problem.id)
        problems = problems.filter(id__in=solved_problem_ids)
    elif status_filter == 'unsolved':
        unsolved_problem_ids = []
        for problem in problems:
            latest_attempt = Attempt.objects.filter(problem=problem).order_by('-date_attempted').first()
            if not latest_attempt or latest_attempt.status != 'Solved':
                unsolved_problem_ids.append(problem.id)
        problems = problems.filter(id__in=unsolved_problem_ids)
    
    easy_problems = problems.filter(difficulty='Easy').order_by('number')
    medium_problems = problems.filter(difficulty='Medium').order_by('number')
    hard_problems = problems.filter(difficulty='Hard').order_by('number')
    
    # Neetcode's topic order
    neetcode_topic_order = [
        "Arrays & Hashing",
        "Two Pointers",
        "Stack",
        "Binary Search",
        "Sliding Window",
        "Linked List",
        "Math & Geometry",
        "Bit Manipulation",
        "Trees",
        "Tries",
        "Backtracking",
        "Heap / Priority Queue",
        "Graphs",
        "Dynamic Programming",
        "Intervals",
        "Greedy"
    ]
    # Only include topics that exist in the DB, in Neetcode's order
    db_topics = list(Problem.objects.values_list('topic', flat=True).distinct())
    all_topics = [topic for topic in neetcode_topic_order if topic in db_topics]
    # Add any extra topics not in the list (just in case)
    all_topics += [topic for topic in db_topics if topic not in all_topics]
    
    context = {
        'easy_problems': easy_problems,
        'medium_problems': medium_problems,
        'hard_problems': hard_problems,
        'all_topics': all_topics,
        'current_difficulty': difficulty_filter,
        'current_topic': topic_filter,
        'current_status': status_filter,
        'search_query': search_query,
    }
    return render(request, 'problems/home.html', context)

def problem_detail(request, problem_id):
    problem = get_object_or_404(Problem, id=problem_id)
    attempts = Attempt.objects.filter(problem=problem).order_by('-date_attempted')
    
    if request.method == 'POST':
        form = AttemptForm(request.POST)
        if form.is_valid():
            attempt = form.save(commit=False)
            attempt.problem = problem
            attempt.save()
            return redirect('problem_detail', problem_id=problem.id)
    else:
        form = AttemptForm()
    
    context = {
        'problem': problem,
        'attempts': attempts,
        'form': form,
    }
    return render(request, 'problems/problem_detail.html', context)

def stats(request):
    total_problems = Problem.objects.count()
    total_attempts = Attempt.objects.count()
    
    solved_problems = []
    for problem in Problem.objects.all():
        latest_attempt = Attempt.objects.filter(problem=problem).order_by('-date_attempted').first()
        if latest_attempt and latest_attempt.status == 'Solved':
            solved_problems.append(problem)
    
    easy_total = Problem.objects.filter(difficulty='Easy').count()
    medium_total = Problem.objects.filter(difficulty='Medium').count()
    hard_total = Problem.objects.filter(difficulty='Hard').count()
    
    easy_solved = len([p for p in solved_problems if p.difficulty == 'Easy'])
    medium_solved = len([p for p in solved_problems if p.difficulty == 'Medium'])
    hard_solved = len([p for p in solved_problems if p.difficulty == 'Hard'])
    
    easy_percent = (easy_solved * 100 // easy_total) if easy_total > 0 else 0
    medium_percent = (medium_solved * 100 // medium_total) if medium_total > 0 else 0
    hard_percent = (hard_solved * 100 // hard_total) if hard_total > 0 else 0
    overall_percent = (len(solved_problems) * 100 // total_problems) if total_problems > 0 else 0
    
    context = {
        'total_problems': total_problems,
        'total_attempts': total_attempts,
        'solved_count': len(solved_problems),
        'overall_percent': overall_percent,
        'easy_total': easy_total,
        'easy_solved': easy_solved,
        'easy_percent': easy_percent,
        'medium_total': medium_total,
        'medium_solved': medium_solved,
        'medium_percent': medium_percent,
        'hard_total': hard_total,
        'hard_solved': hard_solved,
        'hard_percent': hard_percent,
        'recent_attempts': Attempt.objects.all().order_by('-date_attempted')[:5],
    }
    return render(request, 'problems/stats.html', context)