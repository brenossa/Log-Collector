# Log-Collector
Aplicação web com o objetivo de coletar logs de outras aplicações e facilitar o acesso.

## Coletor
Responsável por coletar e armazenar os logs enviados pelos requisitores.

### Features
- [x] Página inicial (ver todos os logs)
- [x] Página para ver log específico (post)
- [x] Página para criar um novo log através do método post
- [x] Salvar posts em um banco de dados
- [] Organizar posts por data
- [] Melhorar apresentação dos logs no site
- [] ...

## Requisitor
Responsável por enviar os logs dos robôs para o coletor.

### Modo de uso
```python
novo_titulo = 'NOME_IDENTIFICADOR_LOG DATA'
novo_conteudo = 'CONTEUDO_LOG'
novo_autor = 'NOME_DO_SEU_ROBO'

obj = LogRequisitor("127.0.0.1", "5000")

obj.criar_novo_post(novo_titulo, novo_conteudo, novo_autor)
```

### Features
- [x] Enviar logs para o site coletor
- [] Criar padrão para logs com informações relevantes que o requisitor possa ler em qualquer robô
- [] ...