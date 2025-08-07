def schedule_jobs(jobs):
    # jobs = [(profit, deadline)]
    jobs.sort(key=lambda x: x[0], reverse=True)
    n = max(job[1] for job in jobs)
    result = [None]*n
    for profit, deadline in jobs:
        for i in range(deadline-1, -1, -1):
            if result[i] is None:
                result[i] = profit
                break
    return sum([p for p in result if p])
