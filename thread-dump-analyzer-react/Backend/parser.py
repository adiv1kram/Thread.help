import re
import json

def parse_thread_dump(dump_content):
    
    
    # This list is initialized at the start to ensure it always exists.
    threads = []
    current_thread = None
    
    # Regex to capture the main information line for a thread
    thread_header_re = re.compile(
        r'"(?P<name>.*?)".*?'
        r'prio=(?P<prio>\d+)\s+'
        r'os_prio=(?P<os_prio>\d+)\s+'
        r'tid=(?P<tid>0x[0-9a-fA-F]+)\s+'
        r'nid=(?P<nid>0x[0-9a-fA-F]+)\s+'
        r'(?P<state>[\w\s\(\)]+?)\s+'
        r'\[(?P<address>0x[0-9a-fA-F]+)\]'
    )
    
    java_lang_thread_state_re = re.compile(r'^\s+java.lang.Thread.State:\s+(?P<java_state>\w+.*)')
    stack_trace_re = re.compile(r'^\s+at\s+(?P<method>.*)')
    lock_info_re = re.compile(r'^\s+-\s+(?P<lock_type>[\w\s]+)\s+<(?P<lock_id>0x[0-9a-fA-F]+)>.*')

    lines = dump_content.splitlines()

    for line in lines:
        header_match = thread_header_re.match(line)
        if header_match:
            if current_thread:
                threads.append(current_thread)
            
            current_thread = header_match.groupdict()
            current_thread['stack_trace'] = []
            current_thread['locks'] = []
            continue

        if current_thread:
            state_match = java_lang_thread_state_re.match(line)
            if state_match:
                current_thread['java_state'] = state_match.group('java_state').strip()
                continue

            stack_match = stack_trace_re.match(line)
            if stack_match:
                current_thread['stack_trace'].append(stack_match.group('method').strip())
                continue

            lock_match = lock_info_re.match(line)
            if lock_match:
                current_thread['locks'].append(lock_match.groupdict())
                continue

    if current_thread:
        threads.append(current_thread)
        
    # The function now correctly returns the (potentially empty) list.
    return threads

if __name__ == '__main__':
    try:
        with open('test_dumps/sample_dump.txt', 'r') as f:
            content = f.read()
            parsed_data = parse_thread_dump(content)
            print(json.dumps(parsed_data, indent=2))
    except FileNotFoundError:
        print("Create a 'test_dumps/sample_dump.txt' file to test the parser.")
