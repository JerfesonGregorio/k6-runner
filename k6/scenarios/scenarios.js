export const completeScenario = {
    scenarios: {
        // Warm-up phase: Constant load for the first 1 minute
        warmup: {
            executor: 'constant-arrival-rate',
            rate: 500,
            timeUnit: '1s',
            duration: '1m',
            preAllocatedVUs: 500,
        },

        // Ramping load: Gradually increases the request rate every 30 seconds
        ramping_load: {
            executor: 'ramping-arrival-rate',
            startRate: 10,
            timeUnit: '1s',
            preAllocatedVUs: 2000,
            maxVUs: 4000,
            stages: [
                { duration: '30s', target: 20 },
                { duration: '30s', target: 30 },
                { duration: '30s', target: 40 },
                { duration: '30s', target: 50 },
                { duration: '30s', target: 60 },
                { duration: '30s', target: 70 },
                { duration: '30s', target: 80 },
                { duration: '30s', target: 90 },
                { duration: '30s', target: 100 },
		{ duration: '30s', target: 110 },
		{ duration: '30s', target: 120 },
		{ duration: '30s', target: 130 },
		{ duration: '30s', target: 140 },
		{ duration: '30s', target: 150 },
		{ duration: '30s', target: 160 },
            ],
        },

        // Spike test: Simulates a sudden burst of traffic for 30 seconds
        spike: {
            executor: 'constant-arrival-rate',
            startTime: '3m',
            rate: 200,
            timeUnit: '1s',
            duration: '30s',
            preAllocatedVUs: 500,
            maxVUs: 1000,
        },

        // Cool-down phase: Slowly reduces traffic back to normal levels
        cooldown: {
            executor: 'ramping-arrival-rate',
            startTime: '3m30s',
            startRate: 100,
            timeUnit: '1s',
            preAllocatedVUs: 300,
            maxVUs: 500,
            stages: [
                { duration: '30s', target: 50 },
                { duration: '30s', target: 30 },
                { duration: '30s', target: 10 },
                { duration: '30s', target: 5 },
            ],
        },
    },
};

export let constantScenario = {
    scenarios: {
        constant_load: {
            executor: 'constant-arrival-rate',
            rate: 100,
            timeUnit: '1s',
            duration: '1000s',
            preAllocatedVUs: 10, 
            maxVUs: 20,
        },
    },
};

export let rampingScenario = {
    scenarios: {
        ramping_load: {
            executor: 'ramping-arrival-rate',
            startRate: 160,
            timeUnit: '1s', 
            preAllocatedVUs: 50, 
            maxVUs: 6000,
            stages: [
		{ duration: '30s', target: 180 },
		{ duration: '30s', target: 200 },
		{ duration: '30s', target: 220 },
		{ duration: '30s', target: 240 },
		{ duration: '30s', target: 260 },
		{ duration: '30s', target: 280 },
		{ duration: '30s', target: 300 },
		{ duration: '30s', target: 320 },
		{ duration: '30s', target: 340 },
		{ duration: '30s', target: 360 },
		{ duration: '30s', target: 380 },
		{ duration: '30s', target: 400 },
            ],
        },
    },
};

export let rampingScenarioSlow = {
    scenarios: {
        ramping_load: {
            executor: 'ramping-arrival-rate',
            startRate: 60,
            timeUnit: '1s', 
            preAllocatedVUs: 10, 
            maxVUs: 6000,
            stages: [
                { duration: '30s', target: 70 },
                { duration: '30s', target: 80 },
                { duration: '30s', target: 90 },
                { duration: '30s', target: 100 },
                { duration: '30s', target: 110 },
{ duration: '30s', target: 120 },
{ duration: '30s', target: 130 },
{ duration: '30s', target: 140 },
{ duration: '30s', target: 150 },
{ duration: '30s', target: 160 },
{ duration: '30s', target: 170 },
            ],
        },
    },
};

export function constantScenarioCustom(rate, timeUnitSeconds, durationSeconds, preAllocatedVUs, maxVUs) {
    return {
        scenarios: {
            constant_load: {
                executor: 'constant-arrival-rate',
                rate: rate,
                timeUnit: `${timeUnitSeconds}s`,
                duration: `${durationSeconds}s`,
                preAllocatedVUs: preAllocatedVUs, 
                maxVUs: maxVUs,
            },
        }
    }
};
