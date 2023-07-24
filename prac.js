const endpoint = 'https://jsonmock.hackerrank.com/api/transactions';

// Function to fetch data from a given page
async function fetchData(page) {
    const url = `${endpoint}?page=${page}`;
    const response = await fetch(url);
    const data = await response.json();
    return data;
}

// Function to fetch data from all the pages recursively
async function fetchAllDataRecursive(page = 1, allData = []) {
    const data = await fetchData(page);

    if (data.data.length === 0) {
        return allData;
    }

    allData = allData.concat(data.data);

    // Recursively fetch data from the next page
    return fetchAllDataRecursive(page + 1, allData);
}


async function maximumTransfer(name, city) {
    const allData = await fetchAllDataRecursive(); // Fetch all the data recursively

    // Filter the data for the given name and city combination
    const filteredData = allData.filter(
        (transaction) =>
            transaction.userName === name && transaction.location.city === city
    );

    // Initialize variables to store the maximum credit and maximum debit amounts
    let maxCredit = 0;
    let maxDebit = 0;

    // Iterate through the filtered data to find the maximum credit and maximum debit amounts
    filteredData.forEach((transaction) => {
        const amount = parseFloat(
            transaction.amount.replace('$', '').replace(',', '')
        );
        if (transaction.txnType === 'credit') {
            maxCredit = Math.max(maxCredit, amount);
        } else if (transaction.txnType === 'debit') {
            maxDebit = Math.max(maxDebit, amount);
        }
    });

    // Return the maximum credit and maximum debit as an object
    return [`\$${maxCredit}`, `\$${maxDebit}`];
}


maximumTransfer("Bob Martin", "Bourg").then((result) => console.log(result));

