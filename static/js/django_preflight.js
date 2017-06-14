"use strict";


jQuery(document).ready(function() {

    function tally() {
        // Tallies the tasks completed
        let $current_state = jQuery('#counter').text();
        let numbified = Number($current_state);
        let tallied = String(numbified+1);
        jQuery('#counter').html(tallied);
    }

    function addToList(new_task) {
        //
        let bullet = jQuery('<ul>').text(new_task);
        bullet.on('click', function(event){
          // event handler for clicking on new_task
          jQuery(this).css('text-decoration', 'line-through');
          tally();
        });
        jQuery('#tasks').append(bullet);
    }


    jQuery('#submit_button').on('click', function(event) {    // Anonymous function for the 2nd parameter
          event.preventDefault();                             // This prevents the form refresh
          let new_task = jQuery('#new_task').val();
          addToList(new_task);
          jQuery('#new_task').val('');
    });
});
