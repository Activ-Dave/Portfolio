<template>
	<v-container>
		<v-row>
			<v-col
			cols="12" lg="6" md="8" sm="12">
				<v-card>
					<v-card-title>Kontakt</v-card-title>
					<v-card-text>
						<v-icon>mdi-phone</v-icon> +48725084649
					</v-card-text>
					<v-card-text>
						<v-icon>mdi-email</v-icon> <a href="mailto:wasi.photograph@gmail.com">wasi.photograph@gamil.com</a>
					</v-card-text>
				</v-card>
			</v-col>
		<v-spacer/>
			<v-col
			cols="12" lg="6" md="8" sm="12">
				<v-card min-height="160">
					<v-card-title>SocialMedia</v-card-title>
					<v-card-actions>
						<v-row justify="center">
							<v-btn text depressed :href='"http://instagram.com/wasi.foto"'><v-icon large>mdi-instagram</v-icon> Wasi.Foto </v-btn>
							<v-btn text depressed :href='"http://facebook.com/wasi.photograph"'><v-icon large>mdi-facebook</v-icon> Wąsi Photograph</v-btn>
						</v-row>
					</v-card-actions>
				</v-card>
			</v-col>
		</v-row>
	</v-container>
</template>

<script>
export default {
	name: 'ContactComponent',
	data: ()=>({
		//
	}),
};
</script>
