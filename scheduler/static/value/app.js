var main = function() {
      $('.socialpost').click(function() {
      var post = $('.status-box').val();
      $('<li>').text(post).prependTo('.posts');
      $('.status-box').val('');
      $('.counter').text('140');
      $('.socialpost').addClass('disabled');
      });
      
      
    $('.status-box').keyup(function() {
    var postLength = $(this).val().length;
    var charactersLeft = 140 - postLength;
    $('.counter').text(charactersLeft);
    
    if(charactersLeft < 0) {
    $('.socialpost').addClass('disabled'); 
    }
    else if(charactersLeft == 140) {
    $('.socialpost').addClass('disabled');
    }
    else {
    $('.socialpost').removeClass('disabled');
    }

  });

    $('.socialpost').addClass('disabled');

};


$(document).ready(main);