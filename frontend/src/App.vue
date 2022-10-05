<template>
	<v-app
	dark>
		<Menu/>
		<v-main>
			<router-view/>
		</v-main>
		<Footer/>	
	</v-app>
</template>

<script>
import Menu from '@/components/Menu';
import Footer from '@/components/Footer';

export default {
	name: 'App',

	components:{
		Menu,
		Footer
	},

	data: () => ({
	//
	}),
};
</script>
