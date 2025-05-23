phrase='''O Impacto da Tecnologia na Sustentabilidade

A tecnologia tem desempenhado um papel crucial na busca por um futuro mais sustentável. Inovações como energias renováveis, redes elétricas inteligentes e veículos elétricos estão reduzindo a dependência de combustíveis fósseis e minimizando as emissões de carbono. Além disso, sensores IoT (Internet das Coisas) permitem o monitoramento em tempo real de recursos naturais, otimizando o uso da água na agricultura e evitando desperdícios. Esses avanços não apenas preservam o meio ambiente, mas também impulsionam economias, criando empregos em setores verdes e incentivando modelos de negócios circulares. A integração entre inovação e sustentabilidade é, portanto, um caminho essencial para enfrentar desafios globais, como as mudanças climáticas.

Contudo, o progresso tecnológico também traz dilemas. A produção em massa de dispositivos eletrônicos gera resíduos difíceis de reciclar, agravando problemas como o acúmulo de lixo tecnológico. Data centers, fundamentais para a era digital, consomem quantidades imensas de energia, muitas vezes proveniente de fontes não renováveis. Além disso, a desigualdade no acesso à tecnologia pode aprofundar disparidades sociais, deixando comunidades marginalizadas sem recursos para adotar soluções sustentáveis. Para que a tecnologia cumpra seu potencial positivo, é necessário priorizar ética, regulamentação rigorosa e investimento em pesquisas que equilibrem inovação e responsabilidade ambiental. Só assim será possível garantir um avanço que beneficie tanto a humanidade quanto o planeta.

'''
print (phrase)
word=input("Please input the word to search for:")

while True:
    if word in phrase:
        print (f"The word {word} is in the phrase.")
        break
    else:
        word=input("The word you're looking for is not in the sentence, try again:\n")