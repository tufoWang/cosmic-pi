// scripts/app.js

new Vue({
    el: '#app',
    data: {
        transaction: {
            sender: '',
            recipient: '',
            amount: null
        },
        transactions: [],
        resources: [],
        summary: {
            total_transactions: 0,
            total_users: 0
        },
        loading: false,
        error: null
    },
    methods: {
        async fetchResources() {
            this.loading = true;
            try {
                const response = await fetch('/api/resources');
                if (!response.ok) throw new Error('Failed to fetch resources');
                this.resources = await response.json();
            } catch (err) {
                this.error = err.message;
            } finally {
                this.loading = false;
            }
        },
        async submitTransaction() {
            this.loading = true;
            this.error = null;
            try {
                const response = await fetch('/api/transactions/new', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(this.transaction)
                });
                if (!response.ok) throw new Error('Transaction failed');
                const result = await response.json();
                this.transactions.push({
                    id: this.transactions.length + 1,
                    ...this.transaction
                });
                this.summary.total_transactions += 1;
                this.resetTransactionForm();
            } catch (err) {
                this.error = err.message;
            } finally {
                this.loading = false;
            }
        },
        resetTransactionForm() {
            this.transaction.sender = '';
            this.transaction.recipient = '';
            this.transaction.amount = null;
        }
    },
    mounted() {
        this.fetchResources();
    }
});
