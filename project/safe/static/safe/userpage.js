content = document.getElementById('content');
        content.addEventListener('click', (e) => {
            if (e.target.tagName == 'BUTTON') {
                id = e.target.getAttribute('id');
                class_name = e.target.getAttribute('class');
                fetch(`/safe/decrypt/${id}/`)
                    .then((response) => {
                        return response.json();
                    })
                    .then(data => {
                        span = document.querySelector('span.' + class_name);
                        span.textContent = data['pass'];
                        e.target.style.display = 'none';
                    })
            }
        });
    
        p = document.querySelector('body > div.container > div.addform > h2');
        form = document.querySelector('.new-cred');
        heading = document.querySelector('#modify');
        p.addEventListener('click', () => {
            if (form.style.display == 'none') {
                form.style.display = 'block';
                heading.innerHTML = `Add new <i class="fas fa-angle-up"></i>`;

            } else {
                form.style.display = 'none';
                heading.innerHTML = `Add new <i class="fas fa-angle-down" ></i>`;
            }
        })

        content = document.querySelector('#content');
        content.addEventListener('click', (e) => {
            e.stopPropagation();
            if (e.target.tagName == 'P') {
                if (e.target.nextElementSibling.style.display == 'block')
                    e.target.nextElementSibling.style.display = 'none';
                else
                    e.target.nextElementSibling.style.display = 'block';
            }
        });

        searchbar=document.querySelector('#searchbar');
        lis=document.querySelectorAll('li');

        searchbar.addEventListener('keyup',()=>{
            lis.forEach(li=>{
                if(li.children[0].textContent.toLowerCase().includes(searchbar.value)){
                    li.style.display='block';
                }
                else
                li.style.display='none';
            })
        })