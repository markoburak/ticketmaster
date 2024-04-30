var cards = document.getElementsByClassName('card');
console.log(cards);
if(cards.length > 0){

    var plus_svg_wrappers = document.getElementsByClassName('svg-wrapper');
    var img_cards = document.getElementsByClassName('img_card');

    function addSVG(current_img) {
      current_id = current_img.id
      id = current_id.split('img_card_').pop();
      var plus_svg_wrapper = document.getElementsByClassName('svg_wrapper');
      plus_svg_wrappers[id-1].style.display = "block";
    }

    function removeSVG(current_img) {
      current_id = current_img.id
      id = current_id.split('img_card_').pop();
      var plus_svg_wrapper = document.getElementsByClassName('svg_wrapper');
      plus_svg_wrappers[id-1].style.display = "none";
    }

};
