$(document).ready(function(){
    $(document).bind('keydown',function(e){
        if ( e.keyCode == 123) {
            e.preventDefault();
            e.returnValue = false;
        }
    });
});

document.onmousedown=disableclick;
function disableclick(event){
    if (event.button==2) {
        return false;
    }
}
function blockRightClick(){

return false;
}


// // 
// Array.prototype.shuffle = function () {
//   var length = this.length;

//   while (length) {
//     var index = Math.floor((length--) * Math.random());
//     var temp = this[length];
//     this[length] = this[index];
//     this[index] = temp;
//   }
//   return this;
// };
//





function check_time() {
  const links = document.getElementsByTagName('a');
  var new_hrefs = [];
  for (var i =1; i < links.length; i++) {
    var you_hrefs = links[i].href
    if (you_hrefs.match('search_query=') == 'search_query=') {
      continue;
}else{
    new_hrefs.push(you_hrefs);}
  }
  
  if (new_hrefs.length == 0) { 
    alert("Check your contents again.");
  return;
  }
  var hrefs = [];
  $.each(new_hrefs,function(i,value){
if(hrefs.indexOf(value) == -1 ) hrefs.push(value);
}

);

// console.log(new_hrefs)


//
  start_times = [];

//
  for (let i = 0; i < hrefs.length; i++) {
    var sksnrl = hrefs[i];
    var sms = sksnrl.split("=");
    var times = sms.pop();
    var start_time = times.replace(/[a-z]/gi, "");
    start_times.push(start_time);
  }


// console.log(start_times)


  var intervals = [];
  for (let i = 0; i < start_times.length; i++) {
    if (i  == start_times.length - 1) {
      interval = 200;
      intervals.push(interval + 1)
      break;
    }
    var interval = start_times[i + 1] - start_times[i]
    intervals.push(interval + 1)
    if (interval < 5) {
      alert('check your contents');
      return;
    }
  }

//   console.log(intervals)
//
  var test_dicts = {};
 var test_arrays = [];
  for (let index = 0; index < hrefs.length; index++) {
    

    var one_key = hrefs[index];
    var one_value = intervals[index];
    test_dicts['url'] = one_key;
    test_dicts['sec'] = one_value;
    test_arrays.push(test_dicts);
    var test_dicts = {};
    continue;

  }


  var time_dict = {};
  var gogo_test = [];
  const start_times_key = [];
  for (let j = 0; j < hrefs.length; j++) {
    time_dict[hrefs[j]] = intervals[j]
  }


  return test_arrays;
}

function get_data_and_open(test_arrays){ (function () {

var test_arrays = check_time(test_arrays);
var test_array = test_arrays.shuffle();
//
function Random2nd(max) {
    return Math.floor(Math.random() * max);
}

function NextIndex(idx, length) {
    return (idx + 1)  % length;
}

// 
function playVideo(url) {
//   console.log('Play:', url);
    var popOption = "scrollbars=no,width=700,height=500,status=no,menubar=no,location=no,toolbar=no"
    objPopup = window.open(url, "Example", popOption);
}


idx = Random2nd(test_array.length),
nextIdx = NextIndex(idx, test_array.length);

playVideo(test_array[idx].url);

(function Loop_loop() {
    setTimeout(function() {
        playVideo(test_array[nextIdx].url);

        idx = nextIdx;
        nextIdx = NextIndex(idx, test_array.length);
        
        Loop_loop();
    }, test_array[idx].sec * 1000);    
})();
})();
}

function close123()
{

location.reload(true);
}



function closechild() {
objPopup.close();
location.reload(true);
}