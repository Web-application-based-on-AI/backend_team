function display(){

alert("I am an alert box!");


}

// If the length of the element's string is 0 then display helper message
   function required(inputtx)
   {
     if (inputtx.value.length == 0)
      {
         alert("message");
         return false;
      }
      return true;
    }