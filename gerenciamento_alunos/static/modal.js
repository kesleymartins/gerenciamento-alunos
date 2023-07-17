document.addEventListener("DOMContentLoaded", () => {
    const modalsLink = document.querySelectorAll('.open-modal')
    const modalFrame = document.querySelector('#modal')

    modalsLink.forEach(element => {
        element.addEventListener('click', event => {
            event.preventDefault()
            
            axios.get(element.getAttribute('href'))
            .then(res => {
                modalFrame.innerHTML = res.data

                const btnClose = modalFrame.querySelector('.btn-close')

                btnClose.addEventListener('click', event => {
                    event.preventDefault()

                    modalFrame.innerHTML = ''
                })
            })
        })
    });
})