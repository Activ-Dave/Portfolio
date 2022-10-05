<template>
	<v-simple-table dense>
		<template v-slot:default>
			<thead>
				<tr>
					<th class="text-left">
					<h3>Usługa</h3></th>
					<th class="text-left">
					<h3>Czas</h3></th>
					<th> 
					<h3>Ilość zdjęć</h3></th>
					<th class="text-right">
					<h3>Cena</h3></th>
				</tr>
			</thead>
			<tbody>
				<tr 
				v-for="item in tariff"
				:key="item.id">
					<td>{{item.name}}</td>
					<td>{{item.time}}</td>
					<td>{{item.much}}</td>
					<td class="text-right">{{item.price}}</td>
				</tr>
			</tbody>
		</template>
	</v-simple-table>
</template>

<script>
import axios from 'axios';

export default{
	name:'TariffComponent',

	data (){
		return{
			tariff:[]
		};
	},

	async created (){
		try{
			const response = await axios.get('http://localhost:8000/api/v1/Tariff/');
			this.tariff = response.data;
		}catch(err){
			console.log(err);
		}
	},
};
</script>
