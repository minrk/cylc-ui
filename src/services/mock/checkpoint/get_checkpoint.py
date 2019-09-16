query = '''
{
    workflows {
        id
        name
        status
        owner
        host
        port
        taskProxies {
            id
            state
            cyclePoint
            task {
                meanElapsedTime
                name
            }
            jobs(sort: { keys: ["submit_num"], reverse:true }) {
                id
                host
                startedTime
                state
                submitNum
            }
        }
    }
}
'''

wrapper = {
    'request_string': query
}

import json
print(json.dumps(wrapper, indent=2))
