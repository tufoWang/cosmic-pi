// components/TransactionForm.js

<template>
    <div>
        <h2>Submit a Transaction</h2>
        <form @submit.prevent="submitTransaction">
            <input type="text" v-model="transaction.sender" placeholder="Sender Address" required>
            <input type="text" v-model="transaction.recipient" placeholder="Recipient Address" required>
            <input type="number" v-model="transaction.amount" placeholder="Amount" required>
            <button type="submit">Send Transaction</button>
        </form>
        <p v-if="error" class="error">{{ error }}</p>
    </div>
</template>

<script>
import { submitTransaction } from '../scripts/api.js';

export default {
    name: 'TransactionForm',
    data() {
        return {
            transaction: {
                sender: '',
                recipient: '',
                amount: null
            },
            error: null
        };
    },
    methods: {
        async submitTransaction() {
            this.error = null;
            try {
                await submitTransaction(this.transaction);
                this.resetForm();
            } catch (err) {
                this.error = err.message;
            }
        },
        resetForm() {
            this.transaction.sender = '';
            this.transaction.recipient = '';
            this.transaction.amount = null;
        }
    }
};
</script>

<style scoped>
.error {
    color: red;
}
</style>
