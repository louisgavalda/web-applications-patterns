<script>
    import {onMount} from 'svelte';

    let notes = [];
    let searchQuery = '';
    let loading = true;

    $: filteredNotes = notes.filter(note =>
        note.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
        note.content.toLowerCase().includes(searchQuery.toLowerCase())
    );

    onMount(async () => {
        try {
            const response = await fetch('http://127.0.0.1:8000/api/notes/');
            if (response.ok) {
                notes = await response.json();
            }
        } catch (error) {
            console.error('Error while loading notes:', error);
        } finally {
            loading = false;
        }
    });
</script>

<svelte:head>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</svelte:head>

<div class="container py-4">
  <!-- Header and Search -->
  <div class="mb-4">
    <h1 class="mb-3">My Notes</h1>
    <input
      type="text"
      bind:value={searchQuery}
      placeholder="Search a note..."
      class="form-control"
    />
  </div>

  <!-- Content -->
  {#if loading}
    <div class="text-center">
      <div class="spinner-border" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
    </div>
  {:else}
    <div class="row g-4">
      {#each filteredNotes as note (note.id)}
        <div class="col-md-6">
          <div class="card h-100">
            <div class="card-body">
              <h5 class="card-title">{note.title}</h5>
              <p class="card-text text-muted">
                {note.content.substring(0, 100)}
                {#if note.content.length > 100}...{/if}
              </p>
              <div class="mb-2">
                {#each note.tags as tag}
                  <span class="badge bg-secondary me-1">{tag.name}</span>
                {/each}
              </div>
              <p class="card-text">
                <small class="text-muted">
                  Last modified on {new Date(note.updated_at).toLocaleDateString('en-US')}
                </small>
              </p>
            </div>
          </div>
        </div>
      {:else}
        <div class="col-12 text-center">
          <p class="text-muted">No notes found</p>
        </div>
      {/each}
    </div>
  {/if}
</div>