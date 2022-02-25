# import sys
# inFile = sys.argv[1]
# outFile = sys.argv[2]

# /Users/alphasingh/Downloads
file = '6'
m = {}
with open(file + '.txt', 'r') as i:
    C, P = map(int, i.readline().split())

    contributors = {}
    for Ci in range(C):
        name_and_skills = i.readline().split()
        # gather contributor name and number of skills
        name = name_and_skills[0]
        contributors[name] = {}
        N = int(name_and_skills[1])
        for Ni in range(N):
            skill_and_level = i.readline().split()
            skill = skill_and_level[0]
            skill_level = int(skill_and_level[1])
            contributors[name][skill] = skill_level

    projects = {}
    for Pi in range(P):
        name, D, S, B, R = map(str, i.readline().split())
        projects[name] = {}
        projects[name]['#score'] = int(S)
        for Ri in range(int(R)):
            skill, level = map(str, i.readline().split())
            if skill not in projects[name]:
                projects[name][skill] = 0
            projects[name][skill] += int(level)

    # print(projects['p17826'])
    # print(contributors['c873'])

    solved_projects = {}
    for project_name, project_skills in projects.items():
        # check if you can complete that project with existing contributors
        remaining_skills = project_skills
        used_contributors = []
        unused_contributors = set(name for name in contributors)
        # print(unused_contributors)
        # keep updating remaining if any skill is met
        for skill in remaining_skills:
            # try to find every contributor that has this skill
            for name in unused_contributors:
                contributor = contributors[name]
                can = name in unused_contributors
                # compare skill levels of contributor with required skill level
                if can and (skill in contributor) and (contributor[skill] >= remaining_skills[skill]):
                    used_contributors.append(name)
                    remaining_skills[skill] = 0
                    unused_contributors.remove(name)
                    break
        # check if all skills were found in some contributors
        if all(level <= 0 for skill, level in remaining_skills.items()):
            solved_projects[project_name] = used_contributors
            # break

    # print('Solved projects:', solved_projects)
    # find maximum scoring project
    # print(scores)
    m = 0
    solved = None
    for project in solved_projects:
        m = max(m, projects[project]['#score'])
        print(m)
        solved = project
        # print()

    with open(file + '_output.txt', 'w') as f:
        if solved:
            f.write('1' + '\n')
            f.write(project + '\n')
            f.write(' '.join(solved_projects[project]) + '\n')
        else:
            f.write('0\n')


"""
3 3
Anna 1
C++ 2
Bob 2
HTML 5
CSS 5
Maria 1
Python 3
Logging 5 10 5 1
C++ 3
WebServer 7 10 7 2
HTML 3
C++ 2
WebChat 10 20 20 2
Python 3
HTML 3
"""