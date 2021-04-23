import axios from 'axios'

import APIBase from './apiBase'


class GetLastColorizedCharacters extends APIBase {
    constructor() {
        super('api/colorify');
    }


    async getLastColorizations() {
        const response = await axios.get(this.getUrl());
        return response.data;
    }
}


class PostCharacterToColorization extends APIBase {
    constructor() {
        super('api/colorify');
    }

    async postCharacters(characters) {  // type: FormData
        const response = await axios.post(
            this.getUrl(),
            characters,
            // {headers: {
            //     'Content-type': 'multipart/form-data'
            // }},
        );
        return response.data;
    }
}


export const $api = {
    getAPI: new GetLastColorizedCharacters(),
    postAPI: new PostCharacterToColorization(),
}