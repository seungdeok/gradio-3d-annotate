<script lang="ts">
	import type { Gradio } from "@gradio/utils";
	import type { LoadingStatus } from "@gradio/statustracker";
	import type { SelectData } from "@gradio/utils";
	import { afterUpdate } from "svelte";
	
	export let value: any = { points: [], tool: null };
	export let value_is_output = false;
	export let label = "";
	export let loading_status: LoadingStatus;
	export let gradio: Gradio<{
		change: never;
		select: SelectData;
		input: never;
		clear_status: LoadingStatus;
	}>;
	export let interactive: boolean = true;

	let pointCount = 0;
	let currentTool = value.tool || null;
	
	$: {
		let parsedValue = value;

		if (typeof value === 'string') {
      try {
        parsedValue = JSON.parse(value);

				pointCount = parsedValue.points.length;
				currentTool = parsedValue.tool;
      } catch (e) {
        console.error("JSON 파싱 오류:", e);
        parsedValue = { points: [], tool: null };
      }
    }
	}
	
	function handle_change(newValue): void {
		const data = {
			...value,
			...newValue
		};
		
		gradio.dispatch("change");
		if (!value_is_output) {
			gradio.dispatch("input");
		}
	}
	
	afterUpdate(() => {
		value_is_output = false;
	});
</script>

<div class="annotate3d-container">
	<!-- {#if label}
		<label class="label">{label}</label>
	{/if} -->
	
	<div class="content">
		<div class="info-panel">
			<div class="status-section">
				<div class="status-item">
					<span class="status-label">Points:</span>
					<span class="status-value">{pointCount}</span>
				</div>
				<div class="status-item">
					<span class="status-label">Active Tool:</span>
					<span class="status-value">{currentTool || '없음'}</span>
				</div>
			</div>
			
			{#if interactive}
				<div class="button-section">
					{#if currentTool === 'BoundingBox' && pointCount > 0}
						<button class="refresh-btn" on:click={() => handle_change({ annotations: [] })}>
							Clear
						</button>
					{/if}
				</div>
			{/if}
		</div>
		
		<div class="placeholder-canvas">
			<div class="placeholder-message">
				{#if pointCount === 0}
					<p>포인트 클라우드 데이터가 없습니다.</p>
					<p>URL을 입력하고 Submit 버튼을 클릭하세요.</p>
				{:else}
					<p>포인트 클라우드 데이터가 로드되었습니다.</p>
				{/if}
			</div>
		</div>
	</div>
</div>

<style>
  .annotate3d-container {
    width: 100%;
    display: flex;
    flex-direction: column;
    font-family: Arial, sans-serif;
  }
  
  .label {
    font-weight: bold;
    margin-bottom: 8px;
  }
  
  .content {
    display: flex;
    flex-direction: column;
    border: 1px solid #ddd;
    border-radius: 4px;
    overflow: hidden;
  }
  
  .info-panel {
    padding: 12px;
    background-color: #f8f9fa;
    border-bottom: 1px solid #ddd;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  
  .status-section {
    flex: 1;
  }
  
  .status-item {
    display: flex;
    margin-bottom: 4px;
  }
  
  .status-label {
    width: 100px;
    font-weight: bold;
    font-size: 12px;
  }
  
  .status-value {
    font-size: 12px;
  }
  
  .button-section {
    display: flex;
    align-items: center;
  }
  
  .refresh-btn {
    padding: 6px 12px;
    background-color: #dc3545;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 12px;
  }
  
  .placeholder-canvas {
    height: 400px;
    background-color: #f0f0f0;
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative;
  }
  
  .placeholder-message {
    text-align: center;
    color: #666;
    line-height: 1.5;
  }
</style>