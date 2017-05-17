import subprocess
import json
import shlex
import pprint
import sys
import logging

def main():
    """This is the main function.
    It is called when __name__ == "__main__"
    :returns: int exit code

    """
#    logging.basicConfig(level=logging.DEBUG)
    try:
        user = sys.ARGV[1]
    except:
        user = 'hmm01i'
    repos = getRepos(user)
    print("%i Personal Repos" % len(repos))
    logging.debug(repos)
    #print("Repo,[size, last update]")
    #for k in repos.keys():
    #    print(str(k),repos[k])

def getRepos(user):
    p = pprint.PrettyPrinter()
    repos = {} # repos by user
    #stats[repo] = query stats (dict) by repos
    
    repos_cmd = 'curl -s https://api.github.com/users/%s/repos' % user
    shlReposCmd = shlex.split(repos_cmd)
    logging.debug(shlReposCmd)

    rsp = subprocess.Popen(shlReposCmd,stdout=subprocess.PIPE).communicate()
    jsonrsp = json.loads(rsp[0])
    for i in jsonrsp:
        if i['fork'] == False:
            repos[i['full_name']]=[i['size'],i['updated_at']]
    return repos

if __name__ == "__main__":
    main()
