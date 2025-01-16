<script>
    import { onMount } from 'svelte';

    let notes = [];
    let tags = [];
    let searchQuery = '';
    let selectedTag = null;
    let loading = true;
    let error = null;

    // TODO: Filter notes based on searchQuery and selectedTag
    $: filteredNotes = notes.filter(note =>
        note.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
        note.content.toLowerCase().includes(searchQuery.toLowerCase())
    );

    // TODO: Implement the fetchNotes function
    async function fetchNotes() {
        loading = true;
        try {
            // Make the application handle search and tag filters.
            const response = await fetch('http://127.0.0.1:8000/api/notes/');
            if (response.ok) {
                notes = await response.json();
            }
        } catch (err) {
            error = 'Failed to fetch notes';
            console.error(err);
        } finally {
            loading = false;
        }
    }

    // TODO: Implement the fetchTags function
    async function fetchTags() {
        try {
            const response = await fetch('http://127.0.0.1:8000/api/tags/');
            if (response.ok) {
                tags = await response.json();
            }
        } catch (err) {
            console.error('Failed to fetch tags:', err);
        }
    }

    // TODO: Implement tag selection handling
    function handleTagSelect(tagName) {
        // Add code to handle tag selection
        // Should we deselect if clicking the same tag?
        // Don't forget to refresh the notes!
    }

    onMount(() => {
        fetchNotes();
        fetchTags();
    });
</script>

<svelte:head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</svelte:head>

<div class="container-fluid">
    <div class="row">
        <!-- Sidebar with tags -->
        <div class="col-md-3 col-lg-2 d-md-block bg-light sidebar">
            <div class="position-sticky pt-3">
                <h6 class="sidebar-heading px-3 mb-1 text-muted">Tags</h6>
                <ul class="nav flex-column">
                    <!-- TODO: Implement the tags list with selection handling -->
                    {#each tags as tag}
                        <li class="nav-item">
                            {tag.name} <a href="#">x</a>
                        </li>
                    {/each}
                </ul>
            </div>
        </div>

        <!-- Main content -->
        <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4">
            <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3">
                <h1>Notes</h1>
            </div>

            <!-- Search bar -->
            <!-- TODO: Implement the search bar with proper binding -->
            <div class="mb-4">
                <input
                    type="text"
                    class="form-control"
                    placeholder="Search notes..."
                    bind:value={searchQuery}
                />
            </div>

            <!-- Notes grid -->
            {#if loading}
                <div class="text-center">
                    <div class="spinner-border" role="status">
                        <span class="visually-hidden">Loading...</span>
                    </div>
                </div>
            {:else if error}
                <div class="alert alert-danger" role="alert">
                    {error}
                </div>
            {:else}
                <div class="row row-cols-1 row-cols-md-2 g-4">
                    <!-- TODO: Implement the notes grid -->
                    {#each filteredNotes as note (note.id)}
                        <div class="col">
                            <div class="card">
                              <div class="card-body">
                                <h5 class="card-title">{ note.title }</h5>
                                <h6 class="card-subtitle mb-2 text-body-secondary">{ note.created_at }</h6>
                                <p class="card-text">{ note.content }</p>
                                <a href="#" class="card-link">Delete</a>
                                <a href="#" class="card-link">Update</a>
                              </div>
                            </div>
                        </div>
                    {/each}
                </div>
            {/if}
        </main>
    </div>
</div>

<style>
    .sidebar {
        height: 100vh;
        border-right: 1px solid #dee2e6;
    }
</style>