Title: LocalStorage with Knockout.js - jQuery Mobile - jStorage
Date: 2012-01-15 23:10
Author: Michael
Category: Blog, code, HTML5, Javascript, jQuery Mobile, knockout, localStorage, Programming, Uncategorized
Slug: localstorage-with-knockout-js-jquery-mobile-jstorage
Status: published

I recently started evaluating various JS libraries/frameworks and other
JavaScript goodies. I just wanted to post a quick tutorial when working
with Phonegap (Cordova) [jQuery Mobile](http://jquerymobile.com/) and
[Knockout.js](http://knockoutjs.com/).

This project uses;

1.  [Cordova](http://incubator.apache.org/projects/callback.html)
2.  [jQuery Mobile](http://jquerymobile.com/)
3.  [Knockout.js](http://knockoutjs.com)
4.  [jStorage](http://www.jstorage.info/)

Set a binding to a click event on the view model you want to save:

``` {lang="javascript"}
/* GLOBAL VAR & CLICK HANDLER/FUNCTION TO STORE ViewModel */
var viewSaveID;
function saveThisViewModel() {
    // check to see if jStorage has items
    // if not, assign 0 to key otherwise assign count number 
// as items are save chronologically and not overwritten
    if ($.jStorage.index().length) === 0) {
        viewSaveID = 0;
    }
    viewSaveID = $.jStorage.index().length;
    // increment counter for key to localStorage
    viewSaveID = viewSaveID + 1;
    // Set data to JS format could also be ko.toJSON for a JSON object
    var data = ko.toJS(myViewModel);
    // on the dollar save via jStorage
    $.jStorage.set(viewSaveID, data);
    // return true to keep default behavior in app
    return true;
}
```

Next I would like to show you how we get the data. Although this
implementation looks incredibly simple, I went through a bunch of
implementations to arrive at this:

``` {lang="javascript"}
/* Get Data From Storage and save it to Array */
function getDataStore() {
// assign the keys of the jStorage index to an observable array
    myViewModel.myDataStoreIndex($.jStorage.index());
    
// check to see if there are items in the data store array
// if yes, remove them 
    if (myViewModel.myDataStore().length > 0) {
// This may not scale well, but for localStorage, we don't need it too.
// the problem is overwriting and double entries, this little diddy solves both
        myViewModel.myDataStore.removeAll();
        console.log("removeAll fired")
    }
    //create a temp object to hold objects that are saved in storage
    var savedData = {};
// iterate through the array of keys
    for (var i = 0; i < myViewModel.myDataStoreIndex().length; i++) {
// pull the objects from storage based on the keys stored in the array
        savedData = $.jStorage.get(myViewModel.myDataStoreIndex()[i]);
// push the saved object to the observable array
        myViewModel.myDataStore.push(savedData);
        console.log("Data has been pushed to vacDataStore " + i + " times.");
// when you iterate on a list view item in jQuery Mobile 
// you have refresh the list. Otherwise it displays incorrectly
        $('#myListView').listview('refresh');
    }
}
```

Now all you need to do is work with the data in the myDataStore
Observable array. I choose to iterate the objects into a list using the
convient foreach and a template. The code is commented and should be
self explanatory. If you have issues or need further clarification don't
hesitate to comment. I will post the full app soon!
