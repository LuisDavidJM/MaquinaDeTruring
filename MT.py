def turingMachine(initial_state, accept_states, reject_states, transitions, input):
    tape = list(input) + ['_']
    head_position = 0
    current_state = initial_state

    while current_state not in accept_states and current_state not in reject_states:
        symbol_under_head = tape[head_position]
        if (current_state, symbol_under_head) in transitions:
            transition = transitions[(current_state, symbol_under_head)]
            tape[head_position] = transition[1]  # Escribe
            head_position += transition[2]  # Se mueve
            current_state = transition[0]  # Nuevo estado
        else:
            current_state = 'q7'

    return current_state in accept_states, ''.join(tape)

initial_state = 'q1'
accept_states = {'q6'}
reject_states = {'q7'}
transitions = {
    ('q1', '0'): ('q2', '_', 1),
    ('q1', 'x'): ('q7', 'x', 1),
    ('q1', '_'): ('q7', '_', 1),
    ('q2', '0'): ('q3', 'x', 1),
    ('q2', 'x'): ('q2', 'x', 1),
    ('q2', '_'): ('q6', '_', 1),
    ('q3', '0'): ('q4', '0', 1),
    ('q3', 'x'): ('q3', 'x', 1),
    ('q3', '_'): ('q5', '_', -1),
    ('q4', '0'): ('q3', 'x', 1),
    ('q4', 'x'): ('q4', 'x', 1),
    ('q4', '_'): ('q7', '_', 1),
    ('q5', '0'): ('q5', '0', -1),
    ('q5', 'x'): ('q5', 'x', -1),
    ('q5', '_'): ('q2', '_', 1),
}

input = '0000'
result, final_tape = turingMachine(initial_state, accept_states, reject_states, transitions, input)
print(f"Entrada: {input}, Aceptación: {result}, Cinta: {final_tape}")

