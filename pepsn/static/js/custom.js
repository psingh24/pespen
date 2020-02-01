$(document).ready(function() {
    // all custom jQuery will go here
    console.log("custom function page loaded")
    $("input:checkbox").on('click', function() {
        // in the handler, 'this' refers to the box clicked on
        var $box = $(this);
        if ($box.is(":checked")) {
          // the name of the box is retrieved using the .attr() method
          // as it is assumed and expected to be immutable
          var group = "input:checkbox[id='" + $box.attr("id") + "']";
          console.log(group)
          // the checked state of the group/box on the other hand will change
          // and the current value is retrieved using .prop() method
          $(group).prop("checked", false);
          $box.prop("checked", true);
        } else {
          $box.prop("checked", false);
        }
      });

      
        // $('#confirmModal').click(function() {
        //   event.preventDefault();
        //   jQuery.noConflict();
        //   $('#myModal').modal('toggle');
        // });

        // $("#overWritePicks").click(function() {
        //   jQuery.noConflict();
        //   $('#myModal').modal('toggle');

        //   console.log($("#picksForm").serialize())

        //   // $.post(url, data=$('#picksForm').serialize(), function(data) {
        //   //   if (data.status == 'ok') {
        //   //     $('#stepDialog').modal('hide');
        //   //     location.reload();
        //   //   }
        //   //   else {
        //   //     $('#stepDialog .modal-content').html(data);
        //   //   }
        //   // });
        // })
});