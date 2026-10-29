# Slide V

para um conjunto ser um campo, se \alpha e \beta estiverem no campo, $$\alpha + \beta$$ e $$\alpha * \beta$$ tambem estarao. Caso n~ao estejam, o conjunto nao sera um campo. Fechamento com rela'c~ao a adi'c~ao e multiplica'cao

Para ser campo, deve seguir todas as 7 propriedades do slide


Espacço vetorial é fechado em relaçao a soma entre vetores e em relaçao a multiplicação entre vetor e escalar

Nao existe inverso multiplicativo par a aoperacao escalar vetor

para identificar se um espaco vetorial existe, olhar elemento nulo, fechamento por adicao e fechamento por multiplicacao entre escalar e vetor

Graficamente, deve conter a origem (elemento nulo), fechamento com relacao a soma e multiplicacao por escalar. Só fazer o desenho para R2 que fica facil de ver, considerar uma reta que nao passa na origem e traçar 2 vetores quaisquer que estejam na reta

Fourrier: funçoes periodicas pode ser representada por combinacao linear de senoides. Ou seja, as senoides correspondem a um espaco vetorial, onde cada senoide é um vetor

Para verificar se vetores sao LI ou não, basta achar o espaço nulo da matriz gerada pela concatenaçao entre os vetores. Ou seja, $Ax = 0$. Se existir $x \neq 0$ que resolva, entao um dos vetores é dependente dos demais, logo é LD.
Pois para ser LI, $$\alpha * u + \beta * v + \gamma *w = 0 \Leftrightarrow u=v=w=0$$
$[u | v | w] * [\alpha, \beta, \gamma]$

Para achar a matriz de rotaçao, basta rodar os vetores da base canonica. (Usar o circulo trigonometrico. $\left[\begin{array}{c}1\\0\end{array}\right]$ -> eixo do sen)

Ex: $\left[\begin{array}{c}0\\1\end{array}\right] \rightarrow \left[\begin{array}{c}cos\theta\\sen\theta\end{array}\right]$; $\left[\begin{array}{c}1\\0\end{array}\right] \rightarrow \left[\begin{array}{c}-sen\theta\\cos\theta\end{array}\right]$

Como [a\\b] = a[1\\0] + b[0\\1] -> R[a\\b] = aR[1\\0] +bR[0\\1] -> aR_1 + bR_2, sendo R_1 a primeira coluna de R. OLu seja -> a[cos\theta\\sen\theta] + b[-sen\theta\\cos\theta]

Espaço coluna é o espaço gerado pelas colunas, ou seja, é o subespaço gerado pelas colunas L.I

# Slide VI

Transformaçao de um vetor é a mltiplicação de uma matriz pelo vetor

Uma transformação que leva um vetor num multiplo dele é o autovetor do vetor e o fator multiplicativo é um autovalor

Uma transformaçao feita por uma matriz diagonal estica as bases

Se uma transformaçao 

2 matriz são similares se representam a mesma transformaçao linear -> possuem os mesmos autoavalores, com autovetores distintos
Ou seja, pensando na rotaçao. Caso rotacione theta os vetores da base canonica e rotacione theta qualquer outro vetor, a transformaçao é a mesma, embora as matrizes empregadas sejam diferentes

norma é a distancia da origem até o ponto que representa o vetor

Toda matiz simetrica pode ser escrita pelo produto de uma matriz transposta por ela mesma $A = R^T.R$

# Slide VII

lembrar que na mudança para base 2, faz-se divisoes sucessivas, pega o resto de tras pra frente e na contraria, multiplica cada elemento por $2^n$

para representar numeros com sinal, considera-se o algarismo mais significativo como o descritor de sinal. 1 para negativo e 0 para positivo. Nesse caso, o máximo sera $n-1$. A representaçao não é a mesma, para encontrar precisa fazer o complemento 2
- Inverte-se a representaçao binaria (troca 0 por 1 e vice-versa)
- Soma-se 1 ao numero resultante.

Ex: Qual a representação binária de -6 num ambiente com 4 bits?
6 em binário com 4 bits é 0110
$[0110]_2 = [1001 + 1] = [1010]$

Para converter numero real, os numeros após a virgula ficam elevados a expoente negativo.
Ex: 101,1
$1*2^2 + 0*2^1 + 1*2^0 + 1*2^{(-1)} = 5,5$. O ultimo é referente a parte decimal

Usnado IEEE para achar o numero representado pelos bits

0 10000000011 1011100100010000000000000000000000000000000000000000
$(−1)^s * 2^{c−1023} * (1 + f)$

sinal: $(-1)^0 = 1$, positivo
$c = 2^10 + 2 + 1 = 1027$
$f=1*2^1/2 + 0*2^{1/4} + 1*2^{1/8} + ...$
A representaçao ficara entao:
$1*2^4* (1+ f)$

Representaçao
$1 \Rightarrow 0 01111111111 00...00$
Andando 1 casa na representação: $0 01111111111 00...01 \Rightarrow 1 + 2^{-52}$

O menor numero representado a partir de cada numero nao é constante. Por exemplo, o menor numero a partir do 100 é $100 + 2^{-50}$

# Slide VIII

$f(x) = \sqrt{x+1} - \sqrt{x}$
Se x for muito grande, f(x) tende a 0
x sera representado como ponto flutuante. Para uma arquitetura limitada pode gerar numeros muito grandes que quando truncados ficam iguais. Entao o resultado que nunca seria 0, no computador vira 0 , perdendo a capacidade de representação do numero

quando acontece subtraçao de numeros proximos, pode-se tentar fazer manipulacoes algebricas para nao subtrair numeros muito proximos

por exemplo, multiplicar por $(\sqrt{x+1} + \sqrt{x})/(\sqrt{x+1} + \sqrt{x})$

Transforma a subtraçao de numeros por soma

quando existe uma alta sensibilidade o erro acaba sofrendo grandes variações

Erro retropropragado: Tentar achar qual a entrada (x) que ao passar pela função, resulte em f^(x). Sendo f^(x) o resultado de f(x) que o computador calculou. Essa nova entrada vai estar deslocada de x por um valor $\delta x$. Esse $\delta x$ é o erro retropropagado

Serie de Taylor: Aproxima uam função por um polinomio em torno de um ponto $x=k$

$p(x) = a_0 + a_1x + ... + a_nx^n$
$P(x)|_{x=a} = f(x)|_{x=a}$
$P(x)'|_{x=a} = f(x)'|_{x=a}$
$P(x)''|_{x=a} = f(x)''|_{x=a}$
.....


Série de McLaurin é um caso particular onde o ponto escolhido é $x=0$


Problema mal condicionado:

$dx/dt = x(t) - t$

Testar $x(t) = t+ 1 \Rightarrow dx/dt = 1 = (t+1) - t = x(t) - t$ (RHS - Right Hand Side da equaçao diferencial nao ordinal)
Atende a condição de $x(0) = 1$

Considerando um pequeno desvio na entrada x(0) = 1 + $\epsilon$

$x(t) = \epsilon e^t + t + 1$
Para $\epsilon = 0$ volta para a solução anterior
Com o passar de t, o termo exponencial começa a crescer, mesmo para epsilon muito pequeno. Ou seja, para um pequeno desvio no dado de entrada, o resultado fica muito diferente em deteerminadas regiões, nesse caso, para $\epsilon$ grande. Ou seja, independe do algoritmo, é algo intrinsico ao problema. Mesmo na solução analitica é possivel observar.

Numero de condicionamento = variaçao relativa da saida em relação a varaição relativa da entrada ao adicionar um pequeno termo na entrada

Ax = b é bem condicionado se o det(A) é grande, ou seja, A é facilmente inversivel. O contrario acontece, quanto mais proximo det(A) for de 0, mais o problema fica mal condicionado

$\left[
    \begin{array}{cc}
        2 & 4\\
        1.00001 & 2
    \end{array}
\right]
\left[
    \begin{array}{c}
        x_1\\
        x_2
    \end{array}
\right] = 
\left[
    \begin{array}{c}
        5\\
        7
    \end{array}
\right]$

Se não fosse pelo 0.00001, o det seria 0 e o sistema impossível. O sistema apresentado algebricamente é possivel, mas é quase impossivel de resolver

# Slide IX

Decomposiçao LU

$Ax = b \Rightarrow LUx = b \Rightarrow \begin{array}{c} Ly = b \rightarrow \\ Ux = y \end{array}$ acha y e aplica na equação de baixo 

$\left[
\begin{array}{ccc}
    2 & 2 & 1\\
    -1 & 1 & 3\\
    1 & 2 & -1
\end{array}\right]
\Rightarrow
\left[
\begin{array}{ccc}
    2 & 2 & 1\\
    0^{(1/2)} & 2 & 3,5\\
    0^{-(1/2)} & 1 & -1,5
\end{array}\right]
\Rightarrow
\left[
\begin{array}{ccc}
    2 & 2 & 1\\
    0 & 2 & 3,5\\
    0 & 0^{-(1/2)} & -3,25
\end{array}
\right]
\Rightarrow
\left\{
    \begin{array}{c}
        U = 
            \left[
            \begin{array}{ccc}
                2 & 2 & 1\\
                0 & 2 & 3,5\\
                0 & 0 & -3,25
            \end{array}
            \right]\\ 
        L = 
            \left[
            \begin{array}{ccc}
                1 & 0 & 0\\
                -1/2 & 1 & 0\\
                1/2 & 1/2 & 1
            \end{array}\right]
    \end{array}
\right.$

Inverte o sinal das multiplicações para gerar U

Multiplicaçao de matriz por coluna resulta em uma coluana que é a combinaçao linear das colunas com os coeficientes sendo os elementos do vetor

Uma linha vezes uma matriz resulta em uma linha que é a combinaçao linear das linhas com os coeficientes sendo os elementos da linha.
A multiplicação entre matrizes pode ser pensada dessa forma, cada linha da matriz da esquerda resultará em uma linha da matriz resultante, cujos elementos serão a combinação linear.
Essa é a explicação de que a matriz L é montada a partir dos multiplicadores do escalonamento com sinal trocado. A multiplicação LU basicamente desfaz o processo de escalonamento, por isso os coeficientes com sinal trocado.
Alem disso ajuda na hora de fazer as multiplicações, como por exemplo, montar uma matriz de permutaçao fica trivial. Sendo 
$P = \left[
            \begin{array}{ccc}
                0 & 1 & 0\\
                0 & 0 & 1\\
                1 & 0 & 0
            \end{array}\right]$ 
, é fácil ver que $PA$ trocará a ordem das linhas de A de forma que a 1ª linha será a 2ª, a 2ª será a 3ª e a 3ª a 1ª

$det(A) = det(LU) = det(L).det(U)$

Como Determinante de matrizes triangulares é o produto dos elementos da diagonal

$det(L) = 1$; 

$det(U) = 2*2*(-3,25)$ 

O numero de condicionamento de uma matriz $\kappa (A) = ||A|| . ||A^{-1}||$ tem relação com o tamanho dos elementos da diagonal principal, numeros pequenos pioram o condicionamento, então realizar pivoteamentos parciais podem melhorar o condicionamento.

O pivoteamento parcial é feito por etapas, o pivo será o elemento da diagonal referente a linha que esta sendo mantida fixa e a ideia do algoritmo é que o pivo seja sempre o maior valor, mas as linhas consideradas é dali para baixo


# Lista Preparatória para prova 
## Elon 3.2

$\alpha \left[ \begin{array}{cc} 1 & 1\\ 0 & 0 \end{array} \right] + 
\beta \left[ \begin{array}{cc} 1 & 0\\ 0 & 1 \end{array} \right]  +
\gamma \left[ \begin{array}{cc} 1 & 1\\ 1 & 1 \end{array} \right]  = 0 \Rightarrow 
\left[ \begin{array}{cc} \alpha + \beta + \gamma & \alpha + \gamma\\ \gamma & \beta + \gamma \end{array} \right] = 0 \Rightarrow \left\{ \begin{array}{cc} \alpha = 0\\ \beta = 0 \\ \gamma =0  \end{array} \right.$

## Schaum 4.101

a)

$P_n(t) = \alpha_0 + \alpha_1 t + ... + \alpha_n t^n$

### L.I?

$\beta_0 + \beta_1 (1+t) + \beta_2 (1+t+t^2) + ... + \beta_n (1 + t + ... + t^n) = 0 \Rightarrow 
(\beta_0 + \beta_1 + ... + \beta_n) + (\beta_1 + ... + \beta_n) t + (\beta_2 + ... + \beta_n) t^2 + ... + \beta_n) t^n = 0$

$\left\{ \begin{array}{c} \beta_0 + \beta_1 + ... + \beta_n = 0 \\ \beta_1 + ... + \beta_n = 0  \\ \beta_2 + ... + \beta_n = 0 \\ ... \\ \beta_n = 0\end{array}\right. \Rightarrow \beta_0 = \beta_1 = ... = \beta_n = 0$


### Gera o espaço?

$(\beta_0  + \beta_1 (1+t) + \beta_2 (1+t+t^2) + ... + \beta_n (1 + t + ... + t^n) = \alpha_0 + \alpha_1 t + ... + \alpha_n t^n$

$\left\{ \begin{array}{c} \beta_0 + \beta_1 + ... + \beta_n = \alpha_0 \\ \beta_1 + ... + \beta_n = \alpha_1 \\ ... \\ \beta_n = \alpha_n\end{array} \right. \Rightarrow \left[ \begin{array}{ccccc} 1 & 1 & 1 & ... & 0\\ 0 & 1 & 1 & ... & 1\\ 0 & 0 & 1 & ... & 1\\ ...\\ 0 & 0 & 0 & ... & 1 \end{array} \right] \left[ \begin{array}{c} \beta_0 \\ \beta_1 \\ \beta_2 \\ ... \\ \beta_n \end{array} \right] = \left[ \begin{array}{c} \alpha_0 \\ \alpha_1 \\ \alpha_2 \\ ... \\ \alpha_n \end{array} \right]$

Como o determinante é diferente de 0, na verdade é igual a 1, pois sendo triangular superior, seu determinante é o produto de todos os elementos da diagonal superior, o sistema é possivel e determinado, então é possivel encontrar uma combinação linear dos elementos da base que chegam em qualquer polinomio de $P_n(t)$

Como são sao L.I e geram o espaço inteiro, o conjunto é uma base

b)

$\left[ \begin{array}{ccccccc} 1 & 0 & 0 & 0 & ... & 0 & 0\\ 1 & 1 & 0 & 0 & ... & 0 & 0\\ 0 & 1 & 1 & 0 &... & 0 & 0\\ ...\\ 0 & 0 & 0 & 0 & ... & 1 & 1 \\ 0 & 0 & 0 & 0 & ... & 0 & 1 \end{array} \right] \left[ \begin{array}{c} \beta_0 \\ \beta_1 \\ \beta_2 \\ ... \\ \beta_{n-1} \end{array} \right] = \left[ \begin{array}{c} \alpha_0 \\ \alpha_1 \\ \alpha_2 \\ ... \\ \alpha_{n-1} \\ \alpha_n \end{array} \right] \Rightarrow \left\{ \begin{array}{c} \beta_0 = \alpha_0\\ \beta_1 = \alpha_1 - \alpha_0 \\ \beta_2 = \beta_2 - \beta_1 \\ ... \\ \beta_k = \alpha_k - \alpha_{k-1} , para k \neq n \\...\\ \beta_{n-1} = \alpha_n \end{array} \right.$

Sendo assim, existe uma dependência entre os coeficientes, de forma que a dimensão gerada por esse espaço será menor que o espaço original
 


Como a quantidade de elementos é n, não é possivel gerar o espaço inteiro, dimensão (n+1). Especificamente, falta o termo independente.


## Schaum Example 5.2

Uma trasformação linear pode ser encontrada aplicando na base de um espaço, vendo como ela se comporta e montando a matriz de transformação. Exemplo na derivada feito em sala. Vai cair algo similar na prova, talvez relacionado a derivada ou ate mesmo generico

Olhar a foto da solução 


## Schaum example 6.1


A transformaçao linear independe de base, porem ao estabelecer um base para um espaco vetorial, é possivel representá-la por matrizes

Ex, a transformaçao F leva (x,y) em (2x + 3y, 4x-5y)

Na base canonica, pode ser representada pela matriz

$\left[ \begin{array}{cc} 2 & 3\\ 4 & -5 \end{array} \right] \left[ \begin{array}{c} x\\ y \end{array} \right]$

A aplicação da transformação nao troca de base. Sendo assim, aplicar a transofrmaçao ao vetor  (1,2) que é o vetor da base S levará para a base canonica, pois (1,2) está na base canonica. (1,2) na base S é o vetor (1,0). Por isso deve-se passar para a base S após aplicar a transformação em (1,2) e encontrar os coeficientes

Os autovalores são associados a transformaçao entao os autovalores das matrizes que representam as transformacoes em bases distintas sera sempre o mesmo


# Slide X

