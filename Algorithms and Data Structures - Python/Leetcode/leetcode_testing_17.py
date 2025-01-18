def letterCombinations(digits):
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    combinations = []
    
    def backtrack(index, current_combination):
        print(f"Entrando em backtrack: index={index}, current={current_combination}")
        
        if len(current_combination) == len(digits):
            result = ''.join(current_combination)
            combinations.append(result)
            print(f"Combinação completa: {result}")
            return
        
        for letter in digit_to_letters[digits[index]]:
            print(f"Tentando letra: {letter}")
            current_combination.append(letter)
            backtrack(index + 1, current_combination)
            removed = current_combination.pop()
            print(f"Removendo letra: {removed}")
    
    backtrack(0, [])
    return combinations

# Exemplo de uso
print(letterCombinations("23"))