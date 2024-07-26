"""
nums = [2,7,11,15]

target = 22

#para cada elemento da lista nums
for i in range(len(nums)):

  #para cada elemento apos o elemento i
  for j in range(i+1, len(nums)):

    if nums[i] + nums[j] == target:

      print([i,j])
"""

nums = [2, 7, 11, 15]
target = 9

tamanho_lista = len(nums)
dicionario_hash = {}

for i in range(tamanho_lista):
    falta = target - nums[i]

    # Se 'falta' está no dicionário, significa que já vimos um número que somado ao atual resulta em 'target'
    if falta in dicionario_hash.keys():
        # dicionario_hash[falta] fornece o índice do número que somado ao número atual resulta em 'target'
        # i é o índice do número atual
        print([dicionario_hash[falta], i])

    # Adiciona o número atual (nums[i]) como chave e seu índice (i) como valor no dicionário
    dicionario_hash[nums[i]] = i