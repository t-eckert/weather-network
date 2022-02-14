<script>
	import Location from "../components/Location.svelte"

	export let locations = {}
</script>

<div class="mx-auto w-full max-w-6xl px-2 pt-4">
	<h1 class="text-3xl">Weather Network</h1>
	<h2>A demo of networking K3s with Consul.</h2>

	<div class="grid grid-cols-2 gap-4 pt-4">
		{#if locations !== null && Object.values(locations).length !== 0}
			{#each Object.values(locations) as location}
				<Location {location} />
			{/each}
		{:else}
			<h3>No locations found.</h3>
		{/if}
	</div>
</div>
