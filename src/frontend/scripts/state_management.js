// scripts/state_management.js

import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

const store = new Vuex.Store({
    state: {
        transactions: [],
        resources: [],
        summary: {
            total_transactions: 0,
            total_users: 0
        }
    },
    mutations: {
        ADD_TRANSACTION(state, transaction) {
            state.transactions.push(transaction);
            state.summary.total_transactions += 1;
        },
        SET_RESOURCES(state, resources) {
            state.resources = resources;
        }
    },
    actions: {
        async fetchResources({ commit }) {
            const resources = await fetchResources(); // Assuming fetchResources is imported from api.js
            commit('SET_RESOURCES', resources);
        },
        async submitTransaction({ commit }, transaction) {
            await submitTransaction(transaction); // Assuming submitTransaction is imported from api.js
            commit('ADD_TRANSACTION', transaction);
        }
    }
});

export default store;
