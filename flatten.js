/* Flatten a nested array 
   flatten([1, [2, [3]]])>>[1, 2, 3]
   flatten([1, ["2", [{}]]])>>[1, "2", {}]*/

function flatten(arr) {

    var result = [];

    for (var i = 0; i < arr.length; i++) {

        if (Array.isArray(arr[i])) {

            result = result.concat(flatten(arr[i]));

        } else {

            result.push(arr[i]);

        }
    }

    return result;
}
