<template>
	<v-card dark min-height="100">
		<v-card-title>
				<v-btn depressed :to="'/'">Wąsi Photograph</v-btn>
		</v-card-title>
			<v-card-actions>
			<v-row justify="center">
				<v-btn text :to="'/galeria'"> Moje zdjęcia </v-btn>
				<v-btn text :to="'/o_mnie'"> O mnie </v-btn>
				<v-btn text :to="'/cennik'"> Cennik </v-btn>
				<v-btn text :to="'/kontakt'"> Kontakt </v-btn>
			</v-row>			
			</v-card-actions>
	</v-card>
</template>

<script>
export default{
	name: 'MainMenu',
	data: () => ({
	//
	}),
};
</script>
