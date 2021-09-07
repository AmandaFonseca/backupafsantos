(function(win,doc){
    'use strict';

    let submit_create = document.querySelector('.btn-success');
    submit_create.addEventListener ('keypress', (event) => {
        let form_create = document.querySelector('.form');
        form_create.querySelectorAll('input').forEach(element => {
            console.log(element);
            element.value = '';
         })
    });




    let email = document.querySelector('#id_email');
    console.log(email);

    email.addEventListener ('keypress', (event) => {
       const keyName = email.value;
       console.log(keyName)
    });

})(window,document);