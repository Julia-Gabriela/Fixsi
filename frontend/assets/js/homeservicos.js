/**
 * Rola o carrossel horizontalmente.
 */
function scrollCarousel(carouselType, direction) {
    const carouselId = carouselType === 'services' ? 'services-carousel' : 'tools-carousel';
    const carousel = document.getElementById(carouselId);
    
    if (!carousel) return;

    const cardWidth = carouselType === 'services' 
        ? carousel.querySelector('.service-card')?.offsetWidth || 220 
        : carousel.querySelector('.tool-card')?.offsetWidth || 220;
    
    const scrollAmount = cardWidth * direction;
    
    carousel.scrollBy({
        left: scrollAmount,
        behavior: 'smooth'
    });
}


/* ========================
   FUNÇÕES DO MODAL (POP-UP)
   ======================== */

/**
 * Abre e preenche o modal de contratação de serviço.
 */
function openServicoModal(nome, imgUrl, avaliacao, totalAvaliacoes) {
    const modal = document.getElementById('servicoModal');
    if (!modal) {
        console.error('Modal de serviço não encontrado! (servicoModal)');
        return;
    }

    modal.querySelector('.modal-professional-image img').src = imgUrl;
    modal.querySelector('.modal-professional-name').textContent = nome;
    modal.querySelector('.modal-professional-rating').textContent = avaliacao + ' Estrelas';
    modal.querySelector('.modal-professional-reviews').textContent = '(' + totalAvaliacoes + ' avaliações)';
    
    modal.style.display = 'block';
}

/**
 * Abre e preenche o modal de aluguel de ferramenta.
 */
function openFerramentaModal(nome, imgUrl, descricao, preco) {
    const modal = document.getElementById('ferramentaModal');
    if (!modal) {
        console.error('Modal de ferramenta não encontrado! (ferramentaModal)');
        return;
    }

    modal.querySelector('.modal-tool-image img').src = imgUrl;
    modal.querySelector('.modal-tool-name').textContent = nome;
    modal.querySelector('.modal-tool-description').textContent = descricao;
    modal.querySelector('.modal-tool-price').textContent = 'R$ ' + preco + '/dia';
    
    modal.style.display = 'block';
}


/**
 * Adiciona os Event Listeners para os botões e modals
 */
document.addEventListener('DOMContentLoaded', function() {
    
    // --- LÓGICA DOS BOTÕES "CONTRATAR" (SERVIÇOS) ---
    const contactButtons = document.querySelectorAll('.service-card .btn-contact');
    
    contactButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault(); // Impede o redirecionamento
            
            const serviceCard = this.closest('.service-card');
            if (!serviceCard) return;

            // Lê os dados dos data-attributes
            const nome = serviceCard.dataset.nome;
            const avaliacao = serviceCard.dataset.avaliacao;
            const totalAvaliacoes = serviceCard.dataset.totalAvaliacoes;
            const imgUrl = serviceCard.querySelector('.service-image img').src;

            openServicoModal(nome, imgUrl, avaliacao, totalAvaliacoes);
        });
    });

    // --- LÓGICA DOS BOTÕES "ALUGAR" (FERRAMENTAS) ---
    const toolButtons = document.querySelectorAll('.tool-card .btn-contact');
    
    toolButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault(); // Impede o redirecionamento
            
            const toolCard = this.closest('.tool-card');
            if (!toolCard) return;

            // Lê os dados dos data-attributes
            const nome = toolCard.dataset.nome;
            const descricao = toolCard.dataset.descricao;
            const preco = toolCard.dataset.preco;
            const imgUrl = toolCard.querySelector('.tool-image img').src;

            openFerramentaModal(nome, imgUrl, descricao, preco);
        });
    });


    // --- LÓGICA PARA FECHAR OS MODALS ---
    const servicoModal = document.getElementById('servicoModal');
    const ferramentaModal = document.getElementById('ferramentaModal');

    // Botão de fechar (X) do modal de serviço
    if (servicoModal) {
        const closeBtnServico = servicoModal.querySelector('.modal-close');
        if (closeBtnServico) {
            closeBtnServico.onclick = function(event) {
                event.preventDefault(); // Impede o redirecionamento
                servicoModal.style.display = 'none';
            }
        }
    }

    // Botão de fechar (X) do modal de ferramenta
    if (ferramentaModal) {
        const closeBtnFerramenta = ferramentaModal.querySelector('.modal-close');
        if (closeBtnFerramenta) {
            closeBtnFerramenta.onclick = function(event) {
                event.preventDefault(); // Impede o redirecionamento
                ferramentaModal.style.display = 'none';
            }
        }
    }

    // Fecha o modal se o usuário clicar fora da caixa de conteúdo
    window.onclick = function(event) {
        if (event.target == servicoModal) {
            servicoModal.style.display = 'none';
        }
        if (event.target == ferramentaModal) {
            ferramentaModal.style.display = 'none';
        }
    }
});