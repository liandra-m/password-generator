## O que é?
Um simples gerador de senhas que permite definir o tamanho, exclusão de caracteres e padrões. Para usar, tudo que precisará é do python 3.x instalado.

## Argumentos  

### --length, -l
  Define o tamanho da senha gerada. Por padrão, é 8.
  
### --exclude, -e
  Define caracteres que não devem ser utilizados na senha gerada. Passe em uma única string separado por espaços, como 'a b c @'.
  
### --pattern, -p
  Define um padrão, se for maior que o tamanho (length) definido, sobrescreve-o, se for menor, o restante será completado aleatoriamente. Caracteres especiais utilizados para gerar um padrão:  
  * @ - Qualquer caractere;  
  * \# - Letras;  
  * ! - Letras maiúsculas;  
  * & - Letras minúsculas;  
  * $ - Caracteres especiais;  
  * \+ - Números;  
  * / - Utilize antes de um caractere especial de padrão, para sobrescrevê-lo. Retornando o próprio caractere;  

### --output, -o
  Salva a senha gerada em um arquivo, sendo que o primeiro parâmetro é para definir o caminho, e o segundo é opcional, para modo de escrita. Por padrão é (a)ppend, mas também pode ser usado (w)rite.

### Exemplos
    python3 pass_generator.py
    python3 pass_generator.py -l 12 -p 'foo@@@N++#'
    python3 pass_generator.py --pattern 'john/@5++
    python3 pass_generator.py -p '!###/@@@+++' --output '/home/user/pass.txt'
    python3 pass_generator.py --pattern '!&&&@#/#5' --length 32 --exclude 'a b c d' -o 'passwords.txt' 'w'