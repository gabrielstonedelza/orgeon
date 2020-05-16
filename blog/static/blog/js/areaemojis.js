window.addEventListener('DOMContentLoaded', () => {
  const mybutton = document.querySelector('a#emoji-button');
  // const mybutton = document.getElementById("emoji-button")
  const picker = new EmojiButton();

  picker.on('emoji', emoji => {
    document.querySelector('textarea').value += emoji;
  });

  mybutton.addEventListener('click', () => {
    picker.pickerVisible ? picker.hidePicker() : picker.showPicker(mybutton);
  });
});    
     
 