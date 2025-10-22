
<p align="center">
  <img src="https://i.imgur.com/Yr00EEf.png" alt="Fixsi Logo" width="400"/>
</p>

O **Fixsi** é uma plataforma digital desenvolvida para conectar pessoas que precisam de serviços com **profissionais autônomos** qualificados.  
Nosso objetivo é unir praticidade, segurança e confiança — tanto para quem busca ajuda quanto para quem oferece suas habilidades.  

Além disso, o Fixsi também oferece um sistema de **aluguel de ferramentas**, ampliando as possibilidades de uso e tornando o processo ainda mais acessível e colaborativo.  

---

![Funcionalidades](https://img.shields.io/badge/🚀%20Funcionalidades-FF700C?style=for-the-badge&labelColor=FF700C&color=FF700C)

- Cadastro completo de **clientes** e **profissionais**
- **Login e autenticação segura** com gerenciamento de sessão  
- **Painel do usuário** com histórico, perfil e funcionalidades específicas  
- **Perfil detalhado** com dados pessoais, bio, avaliações e área de atuação  
- **Sistema de avaliações** ⭐⭐⭐⭐⭐  
- **Aluguel de ferramentas** integrado à plataforma  
- **Termos de uso e políticas de privacidade** integrados ao fluxo de cadastro  
- Validação automática de **CPF**, **idade mínima (18+)** e **endereço via CEP**

---

![Protótipo](https://img.shields.io/badge/🖼️%20Protótipo%20no%20Figma-FF700C?style=for-the-badge&labelColor=FF700C&color=FF700C)

O protótipo do **Fixsi** foi desenvolvido no **Figma**, apresentando todos os fluxos principais — do cadastro ao painel logado.  
A navegação é interativa e ilustra toda a experiência do usuário final.  

🔗 [Visualizar protótipo no Figma](https://www.figma.com/design/bCaY9zgky6N7vh99HIO2wK/Startups---Fixsi?node-id=2-8&t=3gd9lTYCWTS0Sc29-1)

---

![Tecnologias](https://img.shields.io/badge/🛠️%20Tecnologias%20Utilizadas-FF700C?style=for-the-badge&labelColor=FF700C&color=FF700C)

- **Front-end:** HTML, CSS e JavaScript (vanilla)
- **Back-end:** Django (Python)
- **Banco de Dados:** MySQL Workbench
- **Prototipação:** Figma
- **Integrações:** API ViaCEP para preenchimento automático de endereços

---

![Segurança](https://img.shields.io/badge/🔒%20Segurança%20dos%20Dados-FF700C?style=for-the-badge&labelColor=FF700C&color=FF700C)

A segurança dos dados é uma prioridade no Fixsi:
- As **senhas dos usuários são criptografadas** automaticamente pelo sistema de autenticação do Django antes de serem armazenadas no banco de dados.
- As sessões são protegidas por **tokens de autenticação**, evitando acesso não autorizado.
- As informações sensíveis (CPF, e-mail e data de nascimento) são processadas apenas durante o cadastro e jamais exibidas publicamente.

---

![Como rodar o projeto](https://img.shields.io/badge/⚙️%20Como%20Rodar%20o%20Projeto-FF700C?style=for-the-badge&labelColor=FF700C&color=FF700C)

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/fixsi.git
   ```

2. **Acesse a pasta do backend:**
   ```bash
   cd backend
   ```

3. **Crie e ative um ambiente virtual:**
   ```bash
   python -m venv venv
   venv\Scripts\activate   # (Windows)
   source venv/bin/activate   # (Linux/Mac)
   ```

4. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Configure o banco de dados MySQL:**
   - Crie um banco chamado `fixsi_db` no MySQL Workbench.
   - Ajuste o arquivo `settings.py` com seu usuário e senha do MySQL.

6. **Aplique as migrações:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **Crie um superusuário (opcional):**
   ```bash
   python manage.py createsuperuser
   ```

8. **Inicie o servidor:**
   ```bash
   python manage.py runserver
   ```

9. **Acesse no navegador:**
   ```
   http://127.0.0.1:8000/
   ```

---

![Guia de Contribuição](https://img.shields.io/badge/🤝%20Guia%20de%20Contribuição-FF700C?style=for-the-badge&labelColor=FF700C&color=FF700C)

Para contribuir com o projeto, siga o passo a passo disponível no arquivo abaixo:

📄 [Guia de Fork e Contribuição](./GUIA_FORK_FIXSI.txt)

Esse guia explica como **fazer fork**, **clonar o repositório**, **criar branches**, e **enviar pull requests** corretamente, garantindo uma colaboração organizada e segura.

---

![Arquitetura](https://img.shields.io/badge/🏗️%20Arquitetura-FF700C?style=for-the-badge&labelColor=FF700C&color=FF700C)

O projeto segue a arquitetura **MVC (Model–View–Controller)**, garantindo organização, clareza e escalabilidade:
- `Models`: definem as estruturas de dados (Usuário, Perfil, Cliente, Profissional)
- `Views`: processam as regras de negócio e controlam o fluxo entre telas
- `Templates`: representam o front-end integrado ao Django
- `Static`: contém os arquivos estáticos (CSS, JS e imagens)

---

![Equipe](https://img.shields.io/badge/👩‍💻%20Equipe-FF700C?style=for-the-badge&labelColor=FF700C&color=FF700C)

- [Júlia Gabriela](https://github.com/Julia-Gabriela)  
- [Lara Ewellen](https://github.com/Laraewellen)  
- [Luiza Lima](https://github.com/luizalima13)  
- [Maria Eduarda Nunes](https://github.com/marianunx)  
- [Nathalia Gualberto Lopes](https://github.com/ngualbertolopes)  
- [Vitor Hugo Sátiro](https://github.com/vistor-garcia83)  
- [Vinicius Lacerda Soares](https://github.com/volosami)  

---

![Licença](https://img.shields.io/badge/📜%20Licença-FF700C?style=for-the-badge&labelColor=FF700C&color=FF700C)

Este projeto é de uso acadêmico e está protegido por **Copyright © 2025 - Plataforma Fixsi**.  
Todos os direitos reservados.
