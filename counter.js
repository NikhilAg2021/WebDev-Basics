        let c=0;
        function count() 
        {
            c++;     
            document.querySelector('h1').innerHTML=c;
            if(c%10 === 0)
            {
                alert(`Counter is now at ${c}`)
            }
        }

        document.addEventListener('DOMContentLoaded', function(){
            document.querySelector('button').onclick=count; ///run function 'COUNT '(NOT CALLING IT) when button clicked
        })
        
  