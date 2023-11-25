def turingMachine(states, alphabet, tape_alphabet, initial_state, accept_states, reject_states, transitions, input_string):
    tape = list(input_string) + ['_']  # '_' represents a blank symbol
    head_position = 0
    current_state = initial_state

    while current_state not in accept_states and current_state not in reject_states:
        symbol_under_head = tape[head_position]
        if (current_state, symbol_under_head) in transitions:
            transition = transitions[(current_state, symbol_under_head)]
            tape[head_position] = transition[1]  # Write
            head_position += transition[2]  # Move
            current_state = transition[0]  # New State
        else:
            # Transition not defined, reject
            current_state = ''

    return current_state in accept_states, ''.join(tape)

states = {'q0', 'q1', 'q2','q3', 'q4', 'q5', 'q6'}
alphabet = {'0', '1'}
tape_alphabet = {'0', '1', '_'}
initial_state = 'q0'
accept_states = {'q6'}
reject_states = {''}
transitions = {
    ('q0', '0'): ('q1', '_', 1),
    ('q0', '1'): ('q5', '_', 1),
    #('q0', '_'): ('', '', ),
    ('q1', '0'): ('q1', '0', 1),
    ('q1', '1'): ('q2', '1', 1),
    #('q1', '_'): ('', '', ),
    ('q2', '0'): ('q3', '1', -1),
    ('q2', '1'): ('q2', '1', 1),
    ('q2', '_'): ('q4', '_', -1),
    ('q3', '0'): ('q3', '0', -1),
    ('q3', '1'): ('q3', '1', -1),
    ('q3', '_'): ('q0', '_', 1),
    ('q4', '0'): ('q4', '0', -1),
    ('q4', '1'): ('q4', '_', -1),
    ('q4', '_'): ('q6', '0', 1),
    ('q5', '0'): ('q5', '_', 1),
    ('q5', '1'): ('q5', '_', 1),
    ('q5', '_'): ('q6', '_', 1),
}

input_str = '00000000100000'
result, final_tape = turingMachine(states, alphabet, tape_alphabet, initial_state, accept_states, reject_states, transitions, input_str)
print(f"Input: {input_str}, Accepted: {result}, Tape: {final_tape}")
