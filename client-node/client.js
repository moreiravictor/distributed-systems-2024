const minimist = require('minimist');

const args = minimist(process.argv.slice(2));

if (args._[0] === 'publish') {

    const message = args.message;
    const queue = args.queue;

    if (message && queue) {
        console.log(`Publishing message "${message}" to queue "${queue}"`);
        // Add your publishing logic here
    } else {
        console.error('Both -message and -queue arguments are required.');
    }
} else {
    console.error('Unknown command. Use "publish".');
}
