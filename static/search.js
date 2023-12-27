// Begin search.js
let dataJSON;

/**
 * Get the posts lists in json format.
 */
const getPostsJSON = async () => {
    let response = await fetch('http://localhost:8000/api/schedule')
    let data = await response.json()
    return data
}

/**
 * When the user focuses on the search input, the function getPostsJSON is called.
 */
getPostsJSON().then(data => dataJSON = data)
