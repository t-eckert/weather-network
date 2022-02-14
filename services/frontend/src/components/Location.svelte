<script lang="ts">
	import type Location from "../interfaces/Location"

	export let location: Location
</script>

<section class="flex flex-col rounded-md border border-slate-400 px-2 py-1 shadow-md">
	<h3 class="font-semibold">{location?.name}, {location?.sys.country}</h3>
	<span>
		{#each location?.weather as weather}
			<span>{weather.description.charAt(0).toUpperCase() + weather.description.slice(1)}</span>
		{/each}
	</span>
	<span>Feels like {location?.main.feels_like}&deg;C</span>
</section>
