

class APIBase {
    baseUrl = 'http://127.0.0.1:8080';
    resource;

    constructor(resource) {
        if (!resource) throw new Error('Resource is not provided!');
        this.resource = resource;
    }

    getUrl() {
        return `${this.baseUrl}/${this.resource}/`;
    }

    handleErrors(err) {
        console.log({
            message: 'Error ocurred during processing request', err,
        })
    }
}


export default APIBase;
