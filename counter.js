        if (!localStorage.getItem('c'))
        {
            localStorage.setItem('c',0);
        }
        function count() 
        {
            let c = localStorage.getItem('c')
            c++;     
            document.querySelector('h1').innerHTML=c;
            localStorage.setItem('c', c)
        }

        document.addEventListener('DOMContentLoaded', function(){
            document.querySelector('h1').innerHTML=localStorage.getItem('c');
            document.querySelector('button').onclick=count; ///run function 'COUNT '(NOT CALLING IT) when button clicked
        
            
        });
        
  