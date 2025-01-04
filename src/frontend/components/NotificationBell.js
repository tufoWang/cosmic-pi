// components/NotificationBell.js

<template>
    <div class="notification-bell" @click="toggleNotifications">
        <span class="bell-icon">🔔</span>
        <span v-if="hasNotifications" class="notification-count">{{ notificationCount }}</span>
    </div>
</template>

<script>
export default {
    name: 'NotificationBell',
    data() {
        return {
            hasNotifications: false,
            notificationCount: 0
        };
    },
    methods: {
        toggleNotifications() {
            this.hasNotifications = !this.hasNotifications;
            if (this.hasNotifications) {
                this.notificationCount = 0; // Reset count when notifications are viewed
            }
        },
        addNotification() {
            this.notificationCount += 1;
            this.hasNotifications = true;
        }
    }
};
</script>

<style scoped>
.notification-bell {
    cursor: pointer;
    position: relative;
}
.notification-count {
    position: absolute;
    top: -5px;
    right: -10px;
    background: red;
    color: white;
    border-radius: 50%;
    padding: 2px 5px;
}
</style>
