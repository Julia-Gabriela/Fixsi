document.addEventListener('DOMContentLoaded', function() {

    // === 🔹 TOAST PERSONALIZADO ===
    function showToast(message) {
        let toast = document.createElement('div');
        toast.classList.add('toast-alert');
        toast.textContent = message;
        document.body.appendChild(toast);

        setTimeout(() => toast.classList.add('show'), 100);
        setTimeout(() => {
            toast.classList.remove('show');
            setTimeout(() => toast.remove(), 400);
        }, 3000);
    }

    // === 🔹 VERIFICA IDADE (18+) ===
    const dataNascimentoInput = document.getElementById('data_nascimento');
    const btnProximoPasso1 = document.getElementById('btn-proximo-passo1');
    const formPasso1 = document.getElementById('cadastro-form-passo1');

    function validarIdadeEAvisar() {
        if (!dataNascimentoInput || !dataNascimentoInput.value) return false;
        const dataNasc = new Date(dataNascimentoInput.value + "T00:00:00");
        const hoje = new Date();
        const dezoitoAnosAtras = new Date();
        dezoitoAnosAtras.setFullYear(hoje.getFullYear() - 18);
        if (dataNasc <= dezoitoAnosAtras) return true;
        alert('Você precisa ter pelo menos 18 anos para se cadastrar.');
        dataNascimentoInput.value = '';
        dataNascimentoInput.classList.add('erro-input');
        setTimeout(() => dataNascimentoInput.classList.remove('erro-input'), 2000);
        return false;
    }

    if (dataNascimentoInput) dataNascimentoInput.addEventListener('change', validarIdadeEAvisar);

    if (btnProximoPasso1 && formPasso1) {
        btnProximoPasso1.addEventListener('click', function() {
            if (!formPasso1.checkValidity()) {
                formPasso1.reportValidity();
                return;
            }
            if (validarIdadeEAvisar()) {
                window.location.href = '/login/cadastro/passo2/'; // ✅ rota corrigida
            }
        });
    }

    // === 🔹 VALIDA CPF ===
    const cpfInput = document.getElementById('cpf');
    if (cpfInput) {
        cpfInput.addEventListener('blur', function() {
            let cpf = this.value.replace(/\D/g, '');
            if (cpf.length !== 11 || /^(\d)\1+$/.test(cpf)) {
                alert('⚠️ CPF inválido.');
                this.value = '';
                this.classList.add('erro-input');
                setTimeout(() => this.classList.remove('erro-input'), 2000);
                return;
            }
            let soma = 0, resto;
            for (let i = 1; i <= 9; i++) soma += parseInt(cpf.substring(i - 1, i)) * (11 - i);
            resto = (soma * 10) % 11;
            if (resto === 10 || resto === 11) resto = 0;
            if (resto !== parseInt(cpf.substring(9, 10))) {
                alert('⚠️ CPF inválido.');
                this.value = '';
                return;
            }
            soma = 0;
            for (let i = 1; i <= 10; i++) soma += parseInt(cpf.substring(i - 1, i)) * (12 - i);
            resto = (soma * 10) % 11;
            if (resto === 10 || resto === 11) resto = 0;
            if (resto !== parseInt(cpf.substring(10, 11))) {
                alert('⚠️ CPF inválido.');
                this.value = '';
            }
        });
    }

    // === 🔹 AUTO PREENCHER ENDEREÇO PELO CEP ===
    const cepInput = document.getElementById('cep');
    const enderecoInput = document.querySelector('input[name="endereco"]');
    const cidadeInput = document.querySelector('input[name="cidade"]');
    const estadoInput = document.querySelector('input[name="estado"]');

    if (cepInput && enderecoInput && cidadeInput && estadoInput) {
        cepInput.addEventListener('blur', function() {
            let cep = this.value.replace(/\D/g, '');
            if (cep.length !== 8) {
                alert('⚠️ CEP inválido.');
                return;
            }
            fetch(`https://viacep.com.br/ws/${cep}/json/`)
                .then(response => response.json())
                .then(data => {
                    if (data.erro) {
                        alert('⚠️ CEP não encontrado.');
                        return;
                    }
                    enderecoInput.value = data.logradouro || '';
                    cidadeInput.value = data.localidade || '';
                    estadoInput.value = data.uf || '';
                })
                .catch(() => alert('Erro ao buscar o CEP.'));
        });
    }

    // === 🔹 MOSTRA CAMPOS CONFORME TIPO ===
    const radioProfissional = document.getElementById('sou_profissional');
    const radioCliente = document.getElementById('sou_cliente');
    const camposProfissional = document.getElementById('profissional-fields');
    const camposEndereco = document.getElementById('endereco-fields');

    function atualizarCamposVisiveis() {
        if (radioProfissional?.checked) {
            camposProfissional.style.display = 'block';
            camposEndereco.style.display = 'block';
        } else if (radioCliente?.checked) {
            camposProfissional.style.display = 'none';
            camposEndereco.style.display = 'block';
        } else {
            camposProfissional.style.display = 'none';
            camposEndereco.style.display = 'none';
        }
    }

    if (radioProfissional && radioCliente) {
        radioProfissional.addEventListener('change', atualizarCamposVisiveis);
        radioCliente.addEventListener('change', atualizarCamposVisiveis);
        atualizarCamposVisiveis();
    }

    // === 🔹 MODAL DE TERMOS ===
    const btnConcluir = document.getElementById('btn-concluir-cadastro');
    const modal = document.getElementById('modal-termos');
    const btnAceitar = document.getElementById('btn-aceitar-termos');
    const btnRejeitar = document.getElementById('btn-rejeitar-termos');
    const formPasso2 = document.getElementById('cadastro-form');

    if (btnConcluir && modal && btnAceitar && btnRejeitar && formPasso2) {
        btnConcluir.addEventListener('click', function(e) {
            e.preventDefault();
            if (!radioProfissional.checked && !radioCliente.checked) {
                alert("⚠️ Por favor, selecione se você é Cliente ou Profissional.");
                return;
            }
            modal.style.display = 'flex';
        });

        btnAceitar.addEventListener('click', function() {
            modal.style.display = 'none';
            formPasso2.submit(); // 🔥 envia o formulário ao Django
        });

        btnRejeitar.addEventListener('click', function() {
            modal.style.display = 'none';
            window.location.href = '/login/';
        });

        modal.addEventListener('click', function(event) {
            if (event.target === modal) modal.style.display = 'none';
        });
    }

}); // 🔚 DOMContentLoaded
