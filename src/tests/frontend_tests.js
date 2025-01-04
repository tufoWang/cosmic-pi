// src/tests/frontend_tests.js

import { mount } from '@vue/test-utils';
import TransactionForm from '../components/TransactionForm.vue';

describe('TransactionForm.vue', () => {
    it('renders correctly', () => {
        const wrapper = mount(TransactionForm);
        expect(wrapper.exists()).toBe(true);
    });

    it('submits a transaction', async () => {
        const wrapper = mount(TransactionForm);
        await wrapper.setData({
            transaction: {
                sender: 'Alice',
                recipient: 'Bob',
                amount: 50
            }
        });
        await wrapper.find('form').trigger('submit.prevent');
        expect(wrapper.vm.transaction.sender).toBe('');
        expect(wrapper.vm.transaction.recipient).toBe('');
        expect(wrapper.vm.transaction.amount).toBe(null);
    });
});
