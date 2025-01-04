// components/Header.js

<template>
    <header>
        <h1>Cosmic Pi Blockchain Explorer</h1>
        <nav>
            <ul>
                <li><router-link to="/transactions">Transactions</router-link></li>
                <li><router-link to="/resources">Resources</router-link></li>
                <li><router-link to="/analytics">Analytics</router-link></li>
            </ul>
        </nav>
    </header>
</template>

<script>
export default {
    name: 'Header'
};
</script>

<style scoped>
header {
    background: #007bff;
    color: white;
    padding: 10px 20px;
    text-align: center;
}
nav ul {
    list-style: none;
    padding: 0;
}
nav ul li {
    display: inline;
    margin: 0 15px;
}
nav ul li a {
    color: white;
    text-decoration: none;
}
</style>
